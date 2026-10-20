import { afterEach, describe, expect, it } from 'vitest';
import { mkdirSync, mkdtempSync, readFileSync, rmSync, writeFileSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { dirname, join } from 'node:path';
import {
  MANIFESTS,
  bumpSemver,
  bumpVersion,
  latestTagVersion,
  readManifestVersion,
  writeManifestVersion,
} from '../bump-version.ts';

// Fixture copies of each manifest shape, with decoys (dependency versions) that must not change.
const FIXTURES: Record<string, string> = {
  'typescript/package.json': '{\n  "name": "x",\n  "version": "0.1.0",\n  "dependencies": { "a": "1.2.3" },\n  "engines": { "version": "9.9.9" }\n}\n',
  'python/pyproject.toml': '[build-system]\nrequires = ["hatchling"]\nversion = "7.7.7"\n\n[project]\nname = "x"\nversion = "0.1.0"\ndependencies = ["a>=1.2.3"]\n\n[tool.other]\nversion = "5.5.5"\n',
  'java/pom.xml': '<project>\n<modelVersion>4.0.0</modelVersion>\n<groupId>g</groupId>\n<artifactId>a</artifactId>\n<version>0.1.0</version>\n<dependencies><dependency><version>3.0.2</version></dependency></dependencies>\n<build><plugins><plugin><version>3.13.0</version></plugin></plugins></build>\n</project>\n',
  'kotlin/build.gradle.kts': 'plugins {\n    kotlin("jvm") version "2.4.0"\n}\n\ngroup = "com.isaackogan"\nversion = "0.1.0"\n',
  'rust/Cargo.toml': '[package]\nname = "x"\nversion = "0.1.0"\nedition = "2021"\n\n[dependencies]\nserde = { version = "4.4.4" }\n\n[dev-dependencies.y]\nversion = "2.0.0"\n',
  'csharp/src/TikTokShop.Api/TikTokShop.Api.csproj': '<Project>\n  <PropertyGroup>\n    <Version>0.1.0</Version>\n    <TargetFramework>net8.0</TargetFramework>\n  </PropertyGroup>\n  <ItemGroup><PackageReference Include="a" Version="1.2.3" /></ItemGroup>\n</Project>\n',
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
      expect(bumpVersion('go', kind, { root: '.', tags: [] })).toBe('0.1.0');
      expect(bumpVersion('php', kind, { root: '.', tags: ['go/v3.0.0'] })).toBe('0.1.0');
    }
  });
  it('bumps from the latest tag', () => {
    const tags = ['go/v0.1.0', 'go/v0.1.4'];
    expect(bumpVersion('go', 'patch', { root: '.', tags })).toBe('0.1.5');
    expect(bumpVersion('go', 'minor', { root: '.', tags })).toBe('0.2.0');
    expect(bumpVersion('go', 'major', { root: '.', tags })).toBe('1.0.0');
  });
  it('refuses "current" when a tag already exists', () => {
    expect(() => bumpVersion('php', 'current', { root: '.', tags: ['php/v0.1.0'] })).toThrow(/already exists/);
  });
  it('reads real git tags from the repo', () => {
    // Create a throwaway repo so the real one is untouched.
    const root = fixtureRoot();
    const run = (...a: string[]) => git(root, a);
    run('init', '-q');
    run('-c', 'user.name=t', '-c', 'user.email=t@t', 'commit', '-q', '--allow-empty', '-m', 'x');
    run('tag', 'go/v0.3.1');
    expect(bumpVersion('go', 'patch', { root })).toBe('0.3.2');
  });
});

import { execFileSync } from 'node:child_process';
function git(cwd: string, args: string[]): void {
  execFileSync('git', args, { cwd, stdio: 'ignore' });
}
