# Releasing

Every SDK is released from the **release** workflow (`.github/workflows/release.yml`) by pressing a button. This page is the one-time setup it needs, then how to press the button.

## One-time setup

### The `release` environment (do this first)

The publish jobs read their registry secrets from an environment called `release`, so a workflow run from any other branch (whose copy of `release.yml` could be edited) cannot reach them.

- [ ] Create it: **Settings → Environments → New environment**, name `release`.
- [ ] Under **Deployment branches and tags**, choose **Selected branches and tags** and add only `main`.
- [ ] Add every secret below to **this environment** (Environment secrets), not as a repository secret. If you added any as repository secrets before, delete those.
- [ ] Do the same for the `pypi` environment (created in the PyPI step): restrict it to `main`, and put `PYPI_TOKEN` there if you use one.

### Maven Central (Java and Kotlin)

- [ ] Sign in to the [Central Portal](https://central.sonatype.com) and register the namespace `com.isaackogan`.
- [ ] Verify the namespace: the Portal gives you a verification key. Add it as a DNS `TXT` record on `isaackogan.com`, then press **Verify**. (If you don't control that domain, register the `io.github.isaackogan` namespace instead and change the `groupId` in `java/pom.xml` and `kotlin/build.gradle.kts` to match.)
- [ ] Generate a **user token** (Portal → Account → Generate User Token). Store its two halves as the secrets `MAVEN_CENTRAL_USERNAME` and `MAVEN_CENTRAL_PASSWORD`.
- [ ] Create a GPG key: `gpg --full-generate-key`.
- [ ] Publish its public half to a keyserver: `gpg --keyserver keyserver.ubuntu.com --send-keys <KEY_ID>`.
- [ ] Export the private half: `gpg --armor --export-secret-keys <KEY_ID>`. Store it as the secret `MAVEN_GPG_PRIVATE_KEY`, and its passphrase as `MAVEN_GPG_PASSPHRASE`.

### npm (TypeScript)

The workflow publishes with **npm trusted publishing**: no npm token is stored. 0.1.0 was published by hand, because a trusted publisher can only be added to a package that exists.

- [ ] On npmjs.com, open `tiktok-shop-api` → Settings → Trusted Publisher → GitHub Actions, and enter: organization or user `isaackogan`, repository `TikTok-Shop-Api-SDKs`, workflow filename `release.yml`, environment `release`.
- [ ] Optionally, under Settings → Publishing access, choose "Require two-factor authentication and disallow tokens", so only the trusted publisher (and you, with 2FA) can publish.
- [ ] Provenance needs nothing more: the job has `id-token: write`, installs npm 11.5.1 or later, and the repo is public.
- [ ] Because 0.1.0 is already on npm, choose `patch`, `minor` or `major` for TypeScript on the next release. `current` would try to publish 0.1.0 again and fail.

### PyPI (Python)

- [ ] Preferred, no secret: on PyPI add a **trusted publisher** for the project `tiktok-shop-api` (for the first release use *Publishing → Add a new pending publisher*). Owner `isaackogan`, repository `TikTok-Shop-Api-SDKs`, workflow `release.yml`, environment `pypi`.
- [ ] Or the fallback: create an API token on PyPI and store it as `PYPI_TOKEN`. When that secret exists, the job uses it instead.

### crates.io (Rust)

The workflow publishes with **crates.io trusted publishing**: no crates.io token is stored. 0.1.0 was published with an API token, because a trusted publisher can only be added to a crate that exists.

- [ ] Your crates.io account needs a verified email address (Account Settings → Profile), or every publish is refused.
- [ ] On crates.io open `tiktok-shop-api` → Settings → Trusted Publishing → Add, and enter: repository owner `isaackogan`, repository `TikTok-Shop-Api-SDKs`, workflow filename `release.yml`, environment `release`.
- [ ] Because 0.1.0 is already on crates.io, choose `patch`, `minor` or `major` for Rust on the next release. `current` would try to publish 0.1.0 again and fail.

### NuGet (C#)

The workflow publishes with **NuGet trusted publishing**: no NuGet API key is stored.

- [ ] On nuget.org open your account → **Trusted Publishing** → **Create**, and enter: package owner `isaackogan`, CI/CD provider GitHub Actions, repository owner `isaackogan`, repository `TikTok-Shop-Api-SDKs`, workflow file `release.yml`, environment `release`. Under scopes choose **Push → Push new packages and package versions**, and add the package `TikTokShop.Api`.
- [ ] The workflow logs in as the nuget.org user `isaackogan` (`NuGet/login` in `release.yml`). If your nuget.org username differs, change it there.

### Packagist (PHP)

Packagist can't read a subfolder, so `php/` is mirrored to its own repo, and Packagist reads that.

- [ ] Create the **empty** public repository `isaackogan/TikTok-Shop-Api-PHP` (no README, no licence, no `.gitignore`).
- [ ] Make a deploy key: `ssh-keygen -t ed25519 -N "" -C php-mirror -f php-mirror-key`.
- [ ] Add `php-mirror-key.pub` to the mirror repo (Settings → Deploy keys) with **Allow write access** ticked.
- [ ] Store the private half (`php-mirror-key`, the whole file) in *this* repo as the secret `PHP_MIRROR_DEPLOY_KEY`. Then delete the local key files.
- [ ] After the first PHP release has filled the mirror, submit `https://github.com/isaackogan/TikTok-Shop-Api-PHP` at [packagist.org/packages/submit](https://packagist.org/packages/submit). Packagist then picks up each new `v*` tag (enable its GitHub webhook, or let it poll).

### Go

Nothing to set up. The module is `github.com/isaackogan/TikTok-Shop-Api-SDKs/go`, and a `go/vX.Y.Z` tag is the release.

### Branch protection

The release workflow (and the regenerate job in `sdk-generate.yml`) pushes commits to `main` with the built-in `GITHUB_TOKEN`. If `main` is protected, either let GitHub Actions bypass the rules (Settings → Rules → add the *GitHub Actions* app to the bypass list) or exempt the bot, otherwise the release commit and the regenerate commit are rejected. Tags `*/v*` are pushed too, so they must not be blocked by a tag rule.

## Pressing the button

1. Make sure `main` has everything you want to release, and that its last *sdk-generate* run is green (the regenerate commit has landed).
2. Go to **Actions → release → Run workflow**, keep **Use workflow from: main** (any other branch fails at once).
3. For each language pick:

   | Choice | What happens |
   | --- | --- |
   | `skip` (default) | Not released. |
   | `current` | Publish the version already in the manifest, unchanged. Use it for the first `0.1.0`. For Go and PHP (no manifest) it means `0.1.0`, and it is refused if a tag already exists. |
   | `patch` / `minor` / `major` | Bump the manifest and publish that version. For Go and PHP, bump the latest `go/vX.Y.Z` or `php/vX.Y.Z` tag (`0.1.0` when there is none). |

   Manifests: `typescript/package.json`, `python/pyproject.toml`, `java/pom.xml`, `kotlin/build.gradle.kts`, `rust/Cargo.toml`, `csharp/src/TikTokShop.Api/TikTokShop.Api.csproj`. Languages are versioned independently.
4. The workflow then:
   1. computes each version and fails early if its tag already exists;
   2. runs `sdk-generate.yml` for the chosen languages (generate, build, test);
   3. publishes each chosen language to its registry;
   4. for **every language whose publish succeeded** (even if another one failed), commits the bumped manifests (`chore: release <lang>@<ver>, … [skip ci]`), tags `<lang>/vX.Y.Z` (Go and PHP included) and creates a GitHub Release; then the run fails if any chosen publish failed (see below). A language's first release note says it is unofficial, that request signing follows TikTok's documentation but has not been verified against the live API, and asks for an issue if TikTok rejects a signature;
   5. for Go, asks `proxy.golang.org` for the new tag so it is cached.

   The version bump is applied inside each publish job before building, so the published package carries the new version; the repository only gets it in step 4.

### If it fails halfway

Each language is committed, tagged and given a GitHub Release **as soon as its own publish succeeded**, even when another language's publish failed; the run then ends red with an error naming the languages that did not publish. Those are the only ones left to do:

1. Fix the cause (usually a missing or expired secret).
2. Press the button again with **only the failed languages** set (the same choice as before). The already-released ones stay `skip`; their version is now in `main` and tagged, so a second run would bump them again.

Notes for the awkward cases:

- **PHP:** the mirror is pushed before the tag is recorded here. If the `packagist` job pushed the mirror's tag `vX.Y.Z` and then failed, delete that tag on the mirror (`git push <mirror> :refs/tags/vX.Y.Z`) before retrying, or the retry's tag push is rejected.
- **Go:** the `go/vX.Y.Z` tag is pushed with the release commit even when another language failed. If only the final proxy warm-up failed, nothing to redo: run `GOPROXY=proxy.golang.org go list -m github.com/isaackogan/TikTok-Shop-Api-SDKs/go@vX.Y.Z` yourself.
- If the final commit/push itself fails (all three attempts), the packages are live but untagged: make the commit with the bumped files, `git tag <lang>/vX.Y.Z`, push both.
- Tags are placed on the commit pushed after the rebase onto `main`, which may include commits that landed after the SHA the packages were built from.

### What the bump edits

`scripts/bump-version.ts` edits each language's manifest (and Rust's `Cargo.lock` entry) plus the other places that hard-code the version, so they never drift: the `User-Agent` constants in `typescript/src/version.ts`, `python/.../_version.py`, `go/client.go`, `java/.../TikTokShop.java`, `kotlin/.../SigningInterceptor.kt`, `php/src/TikTokShop.php` and `csharp/.../TikTokShopClient.cs`, and the install snippets in the Java and Kotlin READMEs. Rust derives its User-Agent from the crate version. PHP's constant is only the fallback for a checkout: the mirror is pushed before the release commit, so an installed package reports the version Composer recorded. A test also bumps a copy of each language's real files and checks that no test pins the old version. Each locator must match exactly once or the bump fails; a test checks them against the real files.
