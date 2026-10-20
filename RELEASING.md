# Releasing

Every SDK is released from the **release** workflow (`.github/workflows/release.yml`) by pressing a button. This page is the one-time setup it needs, then how to press the button.

## One-time setup

Add each secret under **Settings → Secrets and variables → Actions → New repository secret**.

### Maven Central (Java and Kotlin)

- [ ] Sign in to the [Central Portal](https://central.sonatype.com) and register the namespace `com.isaackogan`.
- [ ] Verify the namespace: the Portal gives you a verification key. Add it as a DNS `TXT` record on `isaackogan.com`, then press **Verify**. (If you don't control that domain, register the `io.github.isaackogan` namespace instead and change the `groupId` in `java/pom.xml` and `kotlin/build.gradle.kts` to match.)
- [ ] Generate a **user token** (Portal → Account → Generate User Token). Store its two halves as the secrets `MAVEN_CENTRAL_USERNAME` and `MAVEN_CENTRAL_PASSWORD`.
- [ ] Create a GPG key: `gpg --full-generate-key`.
- [ ] Publish its public half to a keyserver: `gpg --keyserver keyserver.ubuntu.com --send-keys <KEY_ID>`.
- [ ] Export the private half: `gpg --armor --export-secret-keys <KEY_ID>`. Store it as the secret `MAVEN_GPG_PRIVATE_KEY`, and its passphrase as `MAVEN_GPG_PASSPHRASE`.

### npm (TypeScript)

- [ ] Create an npm automation token (npm → Access Tokens → Granular, with publish rights on `tiktok-shop-api`, or on the whole account for the first publish). Store it as `NPM_TOKEN`.
- [ ] Provenance needs nothing more: the job has `id-token: write`, and the repo must be public.

### PyPI (Python)

- [ ] Preferred, no secret: on PyPI add a **trusted publisher** for the project `tiktok-shop-api` (for the first release use *Publishing → Add a new pending publisher*). Owner `isaackogan`, repository `TikTok-Shop-Api-SDKs`, workflow `release.yml`, environment `pypi`.
- [ ] Or the fallback: create an API token on PyPI and store it as `PYPI_TOKEN`. When that secret exists, the job uses it instead.

### crates.io (Rust)

- [ ] Create an API token at crates.io (Account Settings → API Tokens, scope `publish-new` and `publish-update`). Store it as `CARGO_REGISTRY_TOKEN`.

### NuGet (C#)

- [ ] Create an API key at nuget.org (glob pattern `TikTokShop.Api`, scopes *Push new packages* and *Push package versions*). Store it as `NUGET_TOKEN`.

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
   4. **only if every publish succeeded**, commits the bumped manifests (`chore: release <lang>@<ver>, … [skip ci]`), tags `<lang>/vX.Y.Z` for each (Go and PHP included) and creates a GitHub Release per language. A language's first release note says it is unofficial and that request signing follows TikTok's documentation but has not been verified against the live API;
   5. for Go, asks `proxy.golang.org` for the new tag so it is cached.

   The version bump is applied inside each publish job before building, so the published package carries the new version; the repository only gets it in step 4.

### If it fails halfway

Registries can't unpublish, so a failure after some publishes leaves those languages live but untagged and uncommitted. Fix the cause and run again with **`skip` for the languages already published** and the same choice for the rest. If only the final commit/tag step failed, make the commit and tags by hand (the bumped manifests, `git tag <lang>/vX.Y.Z`, push) rather than re-publishing.

### Not bumped automatically

The bump edits each language's manifest only. A few hand-written strings also carry the version: the `User-Agent` constants in `go/client.go`, `java/.../TikTokShop.java` and `kotlin/.../SigningInterceptor.kt`, and the install snippets in the Java and Kotlin READMEs. Update those in a normal commit when you release.
