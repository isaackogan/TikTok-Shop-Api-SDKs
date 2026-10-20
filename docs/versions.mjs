// Released versions, read from the same manifests scripts/bump-version.ts writes. Code blocks write
// {{version:java}} where a README has the stamped version, so the docs never go stale after a release.
import { readFileSync } from 'node:fs';

const read = (path) => readFileSync(new URL(`../${path}`, import.meta.url), 'utf8');
const match = (path, pattern) => {
  const found = read(path).match(pattern);
  if (!found) throw new Error(`${path}: no version matching ${pattern}`);
  return found[1];
};

export const VERSIONS = {
  java: match('java/pom.xml', /<artifactId>tiktok-shop-api<\/artifactId>\s*<version>(\d+\.\d+\.\d+)<\/version>/),
  kotlin: match('kotlin/build.gradle.kts', /^version = "(\d+\.\d+\.\d+)"$/m),
};

/** Replaces each {{version:<sdk>}} placeholder with that SDK's released version. */
export function stampVersions(text) {
  return text.replace(/\{\{version:(\w+)\}\}/g, (placeholder, sdk) => {
    if (!(sdk in VERSIONS)) throw new Error(`Unknown version placeholder ${placeholder}`);
    return VERSIONS[sdk];
  });
}
