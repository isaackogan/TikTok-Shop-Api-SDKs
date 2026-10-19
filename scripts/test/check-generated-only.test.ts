import { describe, expect, it } from 'vitest';
import { offendingPaths } from '../check-generated-only.ts';

describe('offendingPaths', () => {
  it('allows changes inside a generated folder', () => {
    expect(offendingPaths(' M rust/src/generated/models.rs\n?? go/generated/new.go\n')).toEqual([]);
  });
  it('allows every generated folder and language build folders', () => {
    const ok = [
      'typescript/src/generated/a.ts',
      'python/src/tiktok_shop_api/generated/a.py',
      'go/generated/a.go',
      'java/src/main/java/com/isaackogan/tiktok/shop/generated/A.java',
      'kotlin/src/main/kotlin/com/isaackogan/tiktok/shop/generated/A.kt',
      'php/src/Generated/A.php',
      'rust/src/generated/a.rs',
      'csharp/src/TikTokShop.Api/Generated/A.cs',
      'rust/build/x',
      'go/build/x',
    ];
    expect(offendingPaths(ok.map((p) => ` M ${p}`).join('\n'))).toEqual([]);
  });
  it('flags hand-written files', () => {
    expect(offendingPaths(' M rust/src/lib.rs\n')).toEqual(['rust/src/lib.rs']);
  });
  it('flags a rename whose target leaves a generated folder', () => {
    expect(offendingPaths('R  rust/src/generated/a.rs -> rust/src/a.rs\n')).toEqual(['rust/src/a.rs']);
  });
  it('flags a rename whose source was outside a generated folder', () => {
    expect(offendingPaths('R  rust/src/a.rs -> rust/src/generated/a.rs\n')).toEqual(['rust/src/a.rs']);
  });
  it('flags an untracked file next to a generated folder', () => {
    expect(offendingPaths('?? python/src/tiktok_shop_api/extra.py\n')).toEqual([
      'python/src/tiktok_shop_api/extra.py',
    ]);
  });
  it('does not treat lookalike prefixes as generated', () => {
    expect(offendingPaths('?? go/generated-extra/a.go\n?? go/generated\n')).toEqual([
      'go/generated-extra/a.go',
      'go/generated',
    ]);
  });
  it('flags a directory entry outside generated folders', () => {
    expect(offendingPaths('?? rust/src/\n')).toEqual(['rust/src/']);
  });
  it('handles quoted paths', () => {
    expect(offendingPaths('?? "rust/src/we\\"ird name.rs"\n?? "go/generated/\\303\\251.go"\n')).toEqual([
      'rust/src/we"ird name.rs',
    ]);
  });
  it('handles -z output, including renames (new path first)', () => {
    const z = ' M rust/src/lib.rs\0R  go/generated/new.go\0go/old.go\0?? go/generated/x.go\0';
    expect(offendingPaths(z)).toEqual(['rust/src/lib.rs', 'go/old.go']);
  });
  it('flags path traversal out of a generated folder', () => {
    expect(offendingPaths('?? go/generated/../x.go\n')).toEqual(['go/generated/../x.go']);
  });
  it('ignores empty output', () => {
    expect(offendingPaths('')).toEqual([]);
  });
});
