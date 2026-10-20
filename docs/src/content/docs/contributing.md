---
title: Contributing to the docs
description: Build, validate and maintain the documentation alongside the SDKs and the spec.
---

## Run locally

The documentation is a private Starlight project under `docs/`. Its dependencies and lockfile are separate from the SDK workspace. Building it requires Node.js 22.22 or newer and pnpm 11.5.2.

From the repository root:

```sh
pnpm --dir docs install --frozen-lockfile
pnpm --dir docs dev
```

```sh
pnpm --dir docs check
pnpm --dir docs build
```

`check` verifies the authored pages against the SDKs and the spec:
- **SDK sections.** Every section has the same five pages, and each overview shows its README's install snippet.
- **Code.** Every code block in an SDK's language, under an SDK's tab, or on an SDK's pages is copied from that SDK's README.
- **Counts.** The operation and webhook counts quoted in prose match the spec.
- **The OpenAPI page** lists every tag and documents every vendor extension.

A production build also generates the API reference from the spec, copies the spec into the site for download, and validates internal links with Starlight Links Validator.

## Where to edit

- **Shared pages** are in `docs/src/content/docs/`. `index.mdx` is Getting Started, and `getting-started/` holds the language-neutral guides.
- **Each SDK's section** is in `docs/src/content/docs/sdks/<language>/`. The list of SDKs and section pages is in `docs/sdks.mjs`.
- **The API reference** under `/openapi/reference/` is generated from `.openapi/tiktok-shop.openapi.json` by starlight-openapi. Fix it in the spec's generator, not here; the spec is never edited by hand.

## Code examples

Never write a code example for the docs. Copy it from the SDK's README, whose examples that SDK's own tests compile:

1. **Change the README.** Add or update the example there.
2. **Pass the SDK's tests.** They check that it still compiles.
3. **Copy it into the page.** Use whole blocks, or a contiguous run of whole lines from one, in the same fence language.

`check` rejects any block it can't find in the README, so an example can't drift from the code.

Where a README example contains a released version, write `{{version:java}}` (or `kotlin`) in its place. The build fills in the version from the manifest, so install snippets stay current after each release.

Shell commands use `sh` fences, and language-neutral examples such as the string-to-sign use `text` fences. Neither is checked against a README.

## Verify behavior

Read the hand-written source and its tests before describing behavior. Never use the generated code for this. When the README and the code disagree, the code is right: fix the README in the same change.

Keep the eight sections parallel. A behavior that differs by language belongs on that language's page. A behavior shared by all eight belongs on a Getting Started page.
