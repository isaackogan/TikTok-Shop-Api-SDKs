#!/usr/bin/env bash
# Publishes php/ to the Packagist mirror repo: splits the php/ history into its own branch, pushes it to the
# mirror's main and tags it v<version>. Packagist reads the mirror's tags.
#
#   scripts/split-php.sh <version>          e.g. scripts/split-php.sh 0.1.0
#
# PHP_MIRROR_URL overrides the mirror (default: the real one, over SSH with the deploy key). Needs a full
# clone (not shallow) so `git subtree split` sees the whole history.
set -euo pipefail

version="${1:-}"
if [[ ! "$version" =~ ^[0-9]+\.[0-9]+\.[0-9]+([-+][0-9A-Za-z.-]+)?$ ]]; then
  echo "usage: $0 <version>   (e.g. 0.1.0)" >&2
  exit 2
fi

mirror="${PHP_MIRROR_URL:-git@github.com:isaackogan/TikTok-Shop-Api-PHP.git}"
cd "$(git rev-parse --show-toplevel)"

if [ "$(git rev-parse --is-shallow-repository)" = "true" ]; then
  echo "error: shallow clone; check out with fetch-depth: 0" >&2
  exit 1
fi

branch="split-php-$$"
cleanup() { git branch -D "$branch" >/dev/null 2>&1 || true; }
trap cleanup EXIT

git subtree split --prefix=php -b "$branch" >/dev/null
sha="$(git rev-parse "$branch")"
echo "split php/ at $sha"

# Plain (non-forced) push: the split is deterministic, so every release fast-forwards the mirror.
git push "$mirror" "$branch:refs/heads/main"
git push "$mirror" "$sha:refs/tags/v$version"
echo "pushed php/ to $mirror (main) and tagged v$version"
