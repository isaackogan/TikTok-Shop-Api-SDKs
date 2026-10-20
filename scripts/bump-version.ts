// Computes (and, for manifest languages, writes) the next version of one SDK.
//   tsx scripts/bump-version.ts <lang> <current|patch|minor|major> [--no-write]
// Prints only the resulting version on stdout. Go and PHP have no manifest version: theirs is the latest
// `<lang>/vX.Y.Z` git tag, so nothing is written for them and the release workflow creates the tag.
import { execFileSync } from 'node:child_process';
import { existsSync, readFileSync, writeFileSync } from 'node:fs';
import { join } from 'node:path';
import { fileURLToPath } from 'node:url';
import { LANGS, type Lang } from './lib/meta.ts';

export type Bump = 'current' | 'patch' | 'minor' | 'major';
export const BUMPS: readonly Bump[] = ['current', 'patch', 'minor', 'major'];
/** The version of a language's first release. */
export const FIRST_VERSION = '0.1.0';

const SEMVER = /^(\d+)\.(\d+)\.(\d+)$/;

/** Manifest per language, relative to the repo root. Go and PHP are tag-versioned. */
export const MANIFESTS: Partial<Record<Lang, string>> = {
  typescript: 'typescript/package.json',
  python: 'python/pyproject.toml',
  java: 'java/pom.xml',
  kotlin: 'kotlin/build.gradle.kts',
  rust: 'rust/Cargo.toml',
  csharp: 'csharp/src/TikTokShop.Api/TikTokShop.Api.csproj',
};
export const TAG_VERSIONED: readonly Lang[] = ['go', 'php'];

export function bumpSemver(version: string, kind: Exclude<Bump, 'current'>): string {
  const m = SEMVER.exec(version);
  if (!m) throw new Error(`"${version}" is not a plain X.Y.Z version`);
  const [major, minor, patch] = [Number(m[1]), Number(m[2]), Number(m[3])];
  if (kind === 'major') return `${major + 1}.0.0`;
  if (kind === 'minor') return `${major}.${minor + 1}.0`;
  return `${major}.${minor}.${patch + 1}`;
}

/** Where the version lives in a manifest: a regex whose group 2 is the version, applied inside `scope`. */
interface Locator {
  /** Narrows the text searched: returns the [start, end) slice of the file. */
  scope: (text: string) => [number, number];
  pattern: RegExp;
}

function sectionScope(header: string): (text: string) => [number, number] {
  return (text) => {
    const start = text.search(new RegExp(`^\\[${header}\\]\\s*$`, 'm'));
    if (start < 0) throw new Error(`no [${header}] section`);
    const rest = text.slice(start + 1);
    const next = rest.search(/^\[/m);
    return [start, next < 0 ? text.length : start + 1 + next];
  };
}

const LOCATORS: Partial<Record<Lang, Locator>> = {
  // The first "version" key is the package's own; dependency ranges come later.
  typescript: { scope: (t) => [0, t.length], pattern: /^(\s*"version"\s*:\s*")([^"]+)(")/m },
  python: { scope: sectionScope('project'), pattern: /^(version\s*=\s*")([^"]+)(")/m },
  // The project's own <version> is the first one after <modelVersion> (and after a <parent> block, if any).
  java: {
    scope: (t) => {
      const parentEnd = t.indexOf('</parent>');
      const from = Math.max(t.indexOf('</modelVersion>'), parentEnd >= 0 ? parentEnd : 0);
      const deps = t.search(/<(dependencies|dependencyManagement|build|profiles)>/);
      return [from, deps < 0 ? t.length : deps];
    },
    pattern: /(<version>)([^<]+)(<\/version>)/,
  },
  kotlin: { scope: (t) => [0, t.length], pattern: /^(version\s*=\s*")([^"]+)(")/m },
  rust: { scope: sectionScope('package'), pattern: /^(version\s*=\s*")([^"]+)(")/m },
  csharp: { scope: (t) => [0, t.length], pattern: /(<Version>)([^<]+)(<\/Version>)/ },
};

function locate(lang: Lang, text: string): { index: number; length: number; version: string } {
  const loc = LOCATORS[lang];
  if (!loc) throw new Error(`${lang} has no manifest version`);
  const [start, end] = loc.scope(text);
  const m = loc.pattern.exec(text.slice(start, end));
  if (!m) throw new Error(`no version found in the ${lang} manifest`);
  const index = start + m.index + m[1].length;
  return { index, length: m[2].length, version: m[2] };
}

export function readManifestVersion(lang: Lang, text: string): string {
  return locate(lang, text).version;
}

export function writeManifestVersion(lang: Lang, text: string, version: string): string {
  const { index, length } = locate(lang, text);
  return text.slice(0, index) + version + text.slice(index + length);
}

/** Highest X.Y.Z among tags named `<lang>/vX.Y.Z`, or undefined. */
export function latestTagVersion(lang: Lang, tags: readonly string[]): string | undefined {
  const prefix = `${lang}/v`;
  const versions = tags
    .filter((t) => t.startsWith(prefix) && SEMVER.test(t.slice(prefix.length)))
    .map((t) => t.slice(prefix.length));
  versions.sort((a, b) => {
    const [x, y] = [a, b].map((v) => v.split('.').map(Number));
    return x[0] - y[0] || x[1] - y[1] || x[2] - y[2];
  });
  return versions.at(-1);
}

export function listTags(root: string): string[] {
  return execFileSync('git', ['tag', '--list'], { cwd: root, encoding: 'utf8' })
    .split('\n')
    .map((t) => t.trim())
    .filter(Boolean);
}

/** Cargo.lock is committed and records the crate's own version; keep it in step so `--locked` builds still pass. */
export function syncCargoLock(lockFile: string, version: string): void {
  if (!existsSync(lockFile)) return;
  const text = readFileSync(lockFile, 'utf8');
  const updated = text.replace(/^(name = "tiktok-shop-api"\nversion = ")[^"]+(")/m, `$1${version}$2`);
  if (updated !== text) writeFileSync(lockFile, updated);
}

export interface BumpOptions {
  root: string;
  /** Write the manifest. Defaults to true; tag-versioned languages never write. */
  write?: boolean;
  /** Existing git tags (tag-versioned languages only). Defaults to `git tag --list` in root. */
  tags?: readonly string[];
}

export function bumpVersion(lang: Lang, kind: Bump, opts: BumpOptions): string {
  if (!LANGS.includes(lang)) throw new Error(`unknown language "${lang}"`);
  if (!BUMPS.includes(kind)) throw new Error(`unknown bump "${kind}" (expected ${BUMPS.join('|')})`);

  if (TAG_VERSIONED.includes(lang)) {
    const latest = latestTagVersion(lang, opts.tags ?? listTags(opts.root));
    if (latest === undefined) return FIRST_VERSION;
    if (kind === 'current') {
      throw new Error(`${lang}/v${latest} already exists; "current" only applies to a first release. Choose patch, minor or major.`);
    }
    return bumpSemver(latest, kind);
  }

  const file = join(opts.root, MANIFESTS[lang]!);
  const text = readFileSync(file, 'utf8');
  const current = readManifestVersion(lang, text);
  if (!SEMVER.test(current)) throw new Error(`${lang} manifest version "${current}" is not a plain X.Y.Z`);
  const next = kind === 'current' ? current : bumpSemver(current, kind);
  if (next !== current && opts.write !== false) {
    writeFileSync(file, writeManifestVersion(lang, text, next));
    if (lang === 'rust') syncCargoLock(join(opts.root, 'rust/Cargo.lock'), next);
  }
  return next;
}

if (process.argv[1] && fileURLToPath(import.meta.url) === process.argv[1]) {
  const [lang, kind, ...flags] = process.argv.slice(2);
  try {
    if (!lang || !kind) throw new Error('usage: bump-version.ts <lang> <current|patch|minor|major> [--no-write]');
    const root = fileURLToPath(new URL('../', import.meta.url));
    console.log(bumpVersion(lang as Lang, kind as Bump, { root, write: !flags.includes('--no-write') }));
  } catch (e) {
    console.error(`::error::${(e as Error).message}`);
    process.exit(1);
  }
}
