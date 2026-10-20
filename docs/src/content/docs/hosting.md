---
title: Cloudflare Workers hosting
description: Host the static documentation on Cloudflare Workers static assets under a custom domain.
---

The site is deployed to Cloudflare Workers as static assets and served at `https://tiktok-shop-api.docs.isaackogan.com/`. There is no Worker script: `docs/wrangler.jsonc` only declares the asset directory, the HTML handling and the custom domain. The site needs no Pages Functions, no Cloudflare Astro adapter and no TikTok credentials.

## Configuration

```jsonc
{
  "name": "tiktok-shop-api-docs",
  "compatibility_date": "2026-10-20",
  "assets": {
    "directory": "./dist",
    "html_handling": "auto-trailing-slash",
    "not_found_handling": "404-page"
  },
  "workers_dev": false,
  "routes": [
    { "pattern": "tiktok-shop-api.docs.isaackogan.com", "custom_domain": true }
  ]
}
```

- **`html_handling: auto-trailing-slash`** matches Astro's `trailingSlash: 'always'`. A request for `/sdks/python` redirects to `/sdks/python/`, which serves `sdks/python/index.html`.
- **`not_found_handling: 404-page`** serves Starlight's generated `404.html` with a 404 status.
- **`workers_dev: false`** keeps the site off the `workers.dev` hostname, so the custom domain is the only public origin.
- **The `routes` entry** with `custom_domain: true` makes Cloudflare create the DNS record and the certificate for the hostname on deploy. The `isaackogan.com` zone must be in the same Cloudflare account as the Worker, and the hostname must not already have a DNS record.

`DOCS_SITE` overrides the canonical origin and defaults to the custom domain. `DOCS_BASE` sets a deployment subpath and defaults to `/`. Neither needs to be set for a production build.

The spec files under `/openapi/` are copied from `.openapi/` at build time, so each deploy serves the spec the site was built from.

## Deploy from a checkout

Wrangler is pinned in `docs/package.json`, so the install below provides it. Run `pnpm --dir docs exec wrangler login` once on a new machine.

```sh
pnpm --dir docs install --frozen-lockfile
pnpm --dir docs build
pnpm --dir docs run deploy:cloudflare
```

The first deploy creates the Worker and attaches the custom domain. Later deploys upload only the files that changed.

## Continuous deployment

The documentation workflow, `.github/workflows/docs.yml`, does three things:
- it validates pull requests;
- it uploads the built site as a review artifact;
- on pushes to `main`, it deploys with `cloudflare/wrangler-action`, when the repository has two Actions secrets.

| Secret | Value |
| --- | --- |
| `CLOUDFLARE_API_TOKEN` | A token created from the **Edit Cloudflare Workers** template, scoped to the hosting account and the `isaackogan.com` zone |
| `CLOUDFLARE_ACCOUNT_ID` | The hosting account's ID, shown by `wrangler whoami` |

Without the secrets, the deploy step is skipped and the workflow still validates the build. Forks and pull requests are unaffected.

The spec is regenerated daily. A push that changes `.openapi/` therefore redeploys the site with the new spec and API reference.

## Verify a deployment

```sh
curl -I https://tiktok-shop-api.docs.isaackogan.com/sdks/python/
curl -I https://tiktok-shop-api.docs.isaackogan.com/sdks/python
curl -I https://tiktok-shop-api.docs.isaackogan.com/missing/
curl -I https://tiktok-shop-api.docs.isaackogan.com/openapi/tiktok-shop.openapi.yaml
```

Expect a 200, a 307 redirect to the trailing-slash form, a 404 and a 200, in that order. Then:
- open the site and check the SDK sections and the API reference;
- search for "shop cipher";
- check that the canonical link in the page head uses the custom domain.
