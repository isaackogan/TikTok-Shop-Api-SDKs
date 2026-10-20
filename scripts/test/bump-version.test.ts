import { afterEach, describe, expect, it } from 'vitest';
import { mkdirSync, mkdtempSync, readdirSync, readFileSync, rmSync, writeFileSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';
import { LANGS, type Lang } from '../lib/meta.ts';
import {
  FIRST_VERSION,
  MANIFESTS,
  STAMPS,
  TAG_VERSIONED,
  applyStamps,
  stampFiles,
  bumpSemver,
  bumpVersion,
  latestTagVersion,
  readManifestVersion,
  writeManifestVersion,
} from '../bump-version.ts';

// Fixture copies of each manifest shape, with decoys (dependency versions) that must not change.
const FIXTURES: Record<string, string> = {
  'typescript/package.json': '{\n  "name": "x",\n  "version": "0.1.0",\n  "dependencies": { "a": "1.2.3" },\n  "engines": { "version": "9.9.9" },\n  "nested": {\n    "version": "8.8.8"\n  }\n}\n',
  'python/pyproject.toml': '[build-system]\nrequires = ["hatchling"]\nversion = "7.7.7"\n\n[project]\nname = "x"\nversion = "0.1.0"\ndependencies = ["a>=1.2.3"]\n\n[tool.other]\nversion = "5.5.5"\n',
  'java/pom.xml': '<project>\n<modelVersion>4.0.0</modelVersion>\n<groupId>g</groupId>\n<artifactId>a</artifactId>\n<version>0.1.0</version>\n<dependencies><dependency><version>3.0.2</version></dependency></dependencies>\n<build><plugins><plugin><version>3.13.0</version></plugin></plugins></build>\n</project>\n',
  'kotlin/build.gradle.kts': 'plugins {\n    kotlin("jvm") version "2.4.0"\n}\n\ngroup = "com.isaackogan"\nversion = "0.1.0"\n',
  'rust/Cargo.toml': '[package]\nname = "x"\nversion = "0.1.0"\nedition = "2021"\n\n[dependencies]\nserde = { version = "4.4.4" }\n\n[dev-dependencies.y]\nversion = "2.0.0"\n',
  'csharp/src/TikTokShop.Api/TikTokShop.Api.csproj': '<Project>\n  <PropertyGroup>\n    <Version>0.1.0</Version>\n    <TargetFramework>net8.0</TargetFramework>\n  </PropertyGroup>\n  <ItemGroup><PackageReference Include="a" Version="1.2.3" /></ItemGroup>\n</Project>\n',
  'go/client.go': 'package x\n\tcfg.UserAgent = "tiktok-shop-api-go/0.1.0"\n\t// other/0.1.0\n',
  'typescript/src/version.ts': "export const USER_AGENT = 'tiktok-shop-api-typescript/0.1.0';\n",
  'python/src/tiktok_shop_api/_version.py': '__version__ = "0.1.0"\n',
  'php/src/TikTokShop.php': "    private const VERSION = '0.1.0';\n",
  'csharp/src/TikTokShop.Api/TikTokShopClient.cs': '    public const string UserAgent = "tiktok-shop-api-csharp/0.1.0";\n',
  'java/src/main/java/com/isaackogan/tiktok/shop/TikTokShop.java': 'api.setUserAgent("tiktok-shop-api-java/0.1.0");\n',
  'java/README.md': 'Version `0.1.0`.\n<dependency>\n  <artifactId>tiktok-shop-api</artifactId>\n  <version>0.1.0</version>\n</dependency>\nimplementation \'com.isaackogan:tiktok-shop-api:0.1.0\'\nother 0.1.0\n',
  'kotlin/src/main/kotlin/com/isaackogan/tiktok/shop/SigningInterceptor.kt': 'const val USER_AGENT = "tiktok-shop-api-kotlin/0.1.0"\n',
  'kotlin/README.md': 'implementation("com.isaackogan:tiktok-shop-api-kotlin:0.1.0")\n<artifactId>tiktok-shop-api-kotlin</artifactId>\n  <version>0.1.0</version>\n',
};

const dirs: string[] = [];
function fixtureRoot(): string {
  const root = mkdtempSync(join(tmpdir(), 'bump-'));
  dirs.push(root);
  for (const [p, body] of Object.entries(FIXTURES)) {
    mkdirSync(dirname(join(root, p)), { recursive: true });
    writeFileSync(join(root, p), body);
  }
  return root;
}
afterEach(() => {
  for (const d of dirs.splice(0)) rmSync(d, { recursive: true, force: true });
});

describe('bumpSemver', () => {
  it('bumps each part and resets the lower ones', () => {
    expect(bumpSemver('1.2.3', 'patch')).toBe('1.2.4');
    expect(bumpSemver('1.2.3', 'minor')).toBe('1.3.0');
    expect(bumpSemver('1.2.3', 'major')).toBe('2.0.0');
  });
  it('rejects a pre-release version', () => {
    expect(() => bumpSemver('1.2.3-rc.1', 'patch')).toThrow(/X\.Y\.Z/);
  });
});

describe('manifest languages', () => {
  for (const lang of ['typescript', 'python', 'java', 'kotlin', 'rust', 'csharp'] as const) {
    it(`${lang}: patch edits only the package version`, () => {
      const root = fixtureRoot();
      const file = join(root, MANIFESTS[lang]!);
      const before = readFileSync(file, 'utf8');
      expect(bumpVersion(lang, 'patch', { root })).toBe('0.1.1');
      const after = readFileSync(file, 'utf8');
      expect(after).toBe(before.replace('0.1.0', '0.1.1'));
      expect(readManifestVersion(lang, after)).toBe('0.1.1');
    });
    it(`${lang}: minor and major`, () => {
      const root = fixtureRoot();
      expect(bumpVersion(lang, 'minor', { root })).toBe('0.2.0');
      expect(bumpVersion(lang, 'major', { root })).toBe('1.0.0');
    });
    it(`${lang}: current leaves the file untouched`, () => {
      const root = fixtureRoot();
      const file = join(root, MANIFESTS[lang]!);
      const before = readFileSync(file, 'utf8');
      expect(bumpVersion(lang, 'current', { root })).toBe('0.1.0');
      expect(readFileSync(file, 'utf8')).toBe(before);
    });
    it(`${lang}: write:false computes without editing`, () => {
      const root = fixtureRoot();
      const file = join(root, MANIFESTS[lang]!);
      const before = readFileSync(file, 'utf8');
      expect(bumpVersion(lang, 'major', { root, write: false })).toBe('1.0.0');
      expect(readFileSync(file, 'utf8')).toBe(before);
    });
  }

  it('leaves decoy versions alone', () => {
    const root = fixtureRoot();
    bumpVersion('python', 'major', { root });
    const py = readFileSync(join(root, 'python/pyproject.toml'), 'utf8');
    expect(py).toContain('version = "7.7.7"');
    expect(py).toContain('version = "5.5.5"');
    bumpVersion('rust', 'major', { root });
    const rs = readFileSync(join(root, 'rust/Cargo.toml'), 'utf8');
    expect(rs).toContain('name = "x"\nversion = "1.0.0"');
    expect(rs).toContain('{ version = "4.4.4" }');
    expect(rs).toContain('version = "2.0.0"');
    bumpVersion('java', 'major', { root });
    const pom = readFileSync(join(root, 'java/pom.xml'), 'utf8');
    expect(pom).toContain('<version>3.0.2</version>');
    expect(pom).toContain('<version>3.13.0</version>');
  });

  it('typescript: only the top-level version changes', () => {
    const root = fixtureRoot();
    bumpVersion('typescript', 'major', { root });
    const pkg = readFileSync(join(root, 'typescript/package.json'), 'utf8');
    expect(pkg).toContain('"version": "1.0.0"');
    expect(pkg).toContain('"engines": { "version": "9.9.9" }');
    expect(pkg).toContain('    "version": "8.8.8"');
  });

  it('writeManifestVersion round-trips', () => {
    expect(writeManifestVersion('kotlin', FIXTURES['kotlin/build.gradle.kts'], '4.5.6')).toContain('version = "4.5.6"');
  });

  it('keeps Cargo.lock\'s own entry in step for rust, and only that entry', () => {
    const root = fixtureRoot();
    const lock = join(root, 'rust/Cargo.lock');
    writeFileSync(lock, '[[package]]\nname = "serde"\nversion = "0.1.0"\n\n[[package]]\nname = "tiktok-shop-api"\nversion = "0.1.0"\ndependencies = ["serde"]\n');
    bumpVersion('rust', 'minor', { root });
    expect(readFileSync(lock, 'utf8')).toBe('[[package]]\nname = "serde"\nversion = "0.1.0"\n\n[[package]]\nname = "tiktok-shop-api"\nversion = "0.2.0"\ndependencies = ["serde"]\n');
  });

  it('refuses a pre-release manifest version', () => {
    const root = fixtureRoot();
    writeFileSync(join(root, 'rust/Cargo.toml'), '[package]\nversion = "0.1.0-rc.1"\n');
    expect(() => bumpVersion('rust', 'patch', { root })).toThrow(/X\.Y\.Z/);
  });
});

describe('tag-versioned languages (go, php)', () => {
  it('finds the highest tag numerically, ignoring other prefixes', () => {
    const tags = ['go/v0.9.0', 'go/v0.10.0', 'go/v0.2.0', 'php/v5.0.0', 'v9.9.9', 'go/vnext', 'go/v1.0.0-rc.1'];
    expect(latestTagVersion('go', tags)).toBe('0.10.0');
    expect(latestTagVersion('php', tags)).toBe('5.0.0');
    expect(latestTagVersion('php', ['go/v1.0.0'])).toBeUndefined();
  });
  it('returns 0.1.0 when there is no tag, for every choice', () => {
    for (const kind of ['current', 'patch', 'minor', 'major'] as const) {
      expect(bumpVersion('go', kind, { root: '.', tags: [], write: false })).toBe('0.1.0');
      expect(bumpVersion('php', kind, { root: '.', tags: ['go/v3.0.0'], write: false })).toBe('0.1.0');
    }
  });
  it('bumps from the latest tag', () => {
    const tags = ['go/v0.1.0', 'go/v0.1.4'];
    expect(bumpVersion('go', 'patch', { root: '.', tags, write: false })).toBe('0.1.5');
    expect(bumpVersion('go', 'minor', { root: '.', tags, write: false })).toBe('0.2.0');
    expect(bumpVersion('go', 'major', { root: '.', tags, write: false })).toBe('1.0.0');
  });
  it('refuses "current" when a tag already exists', () => {
    expect(() => bumpVersion('php', 'current', { root: '.', tags: ['php/v0.1.0'], write: false })).toThrow(/already exists/);
  });
  it('reads real git tags from the repo', () => {
    // Create a throwaway repo so the real one is untouched.
    const root = fixtureRoot();
    const run = (...a: string[]) => git(root, a);
    run('init', '-q');
    run('-c', 'user.name=t', '-c', 'user.email=t@t', 'commit', '-q', '--allow-empty', '-m', 'x');
    run('tag', 'go/v0.3.1');
    expect(bumpVersion('go', 'patch', { root })).toBe('0.3.2');
    expect(readFileSync(join(root, 'go/client.go'), 'utf8')).toContain('tiktok-shop-api-go/0.3.2"');
  });
});

describe('version stamps (User-Agent constants, README snippets)', () => {
  const REAL_ROOT = fileURLToPath(new URL('../../', import.meta.url));
  it('are rewritten together with the manifest, and nothing else', () => {
    const root = fixtureRoot();
    bumpVersion('java', 'minor', { root });
    const readme = readFileSync(join(root, 'java/README.md'), 'utf8');
    expect(readme).toBe(FIXTURES['java/README.md'].replaceAll('0.1.0', '0.2.0').replace('other 0.2.0', 'other 0.1.0'));
    expect(readFileSync(join(root, 'java/src/main/java/com/isaackogan/tiktok/shop/TikTokShop.java'), 'utf8')).toContain('java/0.2.0"');
    bumpVersion('kotlin', 'patch', { root });
    expect(readFileSync(join(root, 'kotlin/README.md'), 'utf8')).toBe(FIXTURES['kotlin/README.md'].replaceAll('0.1.0', '0.1.1'));
    bumpVersion('go', 'current', { root, tags: [] });
    expect(readFileSync(join(root, 'go/client.go'), 'utf8')).toContain('other/0.1.0');
  });
  it('are re-synced on "current" when they drifted', () => {
    const root = fixtureRoot();
    writeFileSync(join(root, 'go/client.go'), 'cfg.UserAgent = "tiktok-shop-api-go/0.0.9"\n');
    bumpVersion('go', 'current', { root, tags: [] });
    expect(readFileSync(join(root, 'go/client.go'), 'utf8')).toContain('go/0.1.0"');
  });
  it('are not written with write:false', () => {
    const root = fixtureRoot();
    bumpVersion('kotlin', 'major', { root, write: false });
    expect(readFileSync(join(root, 'kotlin/README.md'), 'utf8')).toBe(FIXTURES['kotlin/README.md']);
  });
  it('fail loudly when a locator matches nothing or twice', () => {
    const root = fixtureRoot();
    writeFileSync(join(root, 'go/client.go'), 'nothing here\n');
    expect(() => bumpVersion('go', 'current', { root, tags: [] })).toThrow(/expected 1 match/);
    writeFileSync(join(root, 'go/client.go'), '"tiktok-shop-api-go/0.1.0"\n"tiktok-shop-api-go/0.1.0"\n');
    expect(() => bumpVersion('go', 'current', { root, tags: [] })).toThrow(/found 2/);
  });
  for (const lang of Object.keys(STAMPS) as Array<keyof typeof STAMPS>) {
    it(`${lang}: every locator matches the real files exactly once (drift guard)`, () => {
      const found = applyStamps(REAL_ROOT, lang, undefined);
      expect(found.length).toBeGreaterThan(0);
      if (!TAG_VERSIONED.includes(lang)) {
        const manifest = readManifestVersion(lang, readFileSync(join(REAL_ROOT, MANIFESTS[lang]!), 'utf8'));
        expect(new Set(found)).toEqual(new Set([manifest]));
      }
    });
  }
  it('are all listed in the release workflow\'s git add', () => {
    const wf = readFileSync(join(REAL_ROOT, '.github/workflows/release.yml'), 'utf8');
    for (const f of [...Object.values(MANIFESTS), ...Object.keys(STAMPS).flatMap((l) => stampFiles(l as 'go'))]) {
      expect(wf, f).toContain(f);
    }
  });
});

describe('no language test pins a version (I7)', () => {
  const REAL_ROOT = fileURLToPath(new URL('../../', import.meta.url));
  // Each language's test sources. A literal of the current version in any of them breaks CI after the first bump.
  const TESTS: Record<Lang, string[]> = {
    typescript: ['typescript/test'],
    python: ['python/tests'],
    go: ['go'],
    java: ['java/src/test'],
    kotlin: ['kotlin/src/test'],
    rust: ['rust/tests', 'rust/examples'],
    php: ['php/tests'],
    csharp: ['csharp/tests'],
  };
  const isTest = (lang: Lang, file: string): boolean =>
    lang === 'go' ? file.endsWith('_test.go') && !file.includes('/generated/') && !file.includes('/build/') : /\.(ts|py|java|kt|rs|php|cs)$/.test(file);
  const files = (dir: string): string[] =>
    readdirSync(dir, { withFileTypes: true }).flatMap((e) => {
      const p = join(dir, e.name);
      if (e.isDirectory()) return ['node_modules', 'bin', 'obj', '__pycache__', 'build', 'generated'].includes(e.name) ? [] : files(p);
      return [p];
    });

  for (const lang of LANGS) {
    it(`${lang}: a patch bump of a copy of the real files leaves no test pinned to the old version`, () => {
      // Copy the real manifest (and Cargo.lock) and every stamped file into a temp root, and bump that.
      const root = mkdtempSync(join(tmpdir(), 'bump-real-'));
      dirs.push(root);
      const copied = [MANIFESTS[lang], ...stampFiles(lang), lang === 'rust' ? 'rust/Cargo.lock' : undefined].filter((f): f is string => !!f);
      for (const f of copied) {
        mkdirSync(dirname(join(root, f)), { recursive: true });
        writeFileSync(join(root, f), readFileSync(join(REAL_ROOT, f)));
      }
      const tagged = TAG_VERSIONED.includes(lang);
      const old = tagged ? FIRST_VERSION : readManifestVersion(lang, readFileSync(join(REAL_ROOT, MANIFESTS[lang]!), 'utf8'));
      const next = bumpVersion(lang, 'patch', { root, tags: tagged ? [`${lang}/v${old}`] : undefined });
      expect(next).not.toBe(old);
      // Every stamp now says the new version.
      if (STAMPS[lang]) expect(new Set(applyStamps(root, lang, undefined))).toEqual(new Set([next]));
      // And no test of the language spells the old one.
      const literal = new RegExp(`(?<![\\w.])${old.replace(/\./g, '\\.')}(?![\\w.])`);
      const pinned = TESTS[lang]
        .flatMap((d) => files(join(REAL_ROOT, d)))
        .filter((f) => isTest(lang, f.slice(REAL_ROOT.length)))
        .filter((f) => literal.test(readFileSync(f, 'utf8')));
      expect(pinned.map((f) => f.slice(REAL_ROOT.length))).toEqual([]);
    });
  }
});

import { execFileSync } from 'node:child_process';
function git(cwd: string, args: string[]): void {
  execFileSync('git', args, { cwd, stdio: 'ignore' });
}
