# Documentation

The site uses Astro Starlight, starlight-openapi and Starlight Links Validator. Its dependencies are isolated from the SDK workspace.

Use Node.js 22.22 or newer and pnpm 11.5.2. From the repository root:

```sh
pnpm --dir docs install --frozen-lockfile
pnpm --dir docs dev
```

Validate and build:

```sh
pnpm --dir docs check
pnpm --dir docs build
pnpm --dir docs preview
```

Authored pages live in `src/content/docs/`. The API reference under `/openapi/reference/` is generated at build time from `.openapi/tiktok-shop.openapi.json`, and the build copies both spec files into `public/openapi/` (ignored by Git) so the site serves them as downloads. Do not edit the spec or copy it into the content directory.

`check` verifies that each SDK section has the same pages, that every code example is copied from that SDK's README (whose examples the SDK's own tests compile), that the counts quoted in prose match the spec, and that no page links the private generator repository. `build` also validates links and generates the search index. See the site's contributing page for authoring and deployment details.

## Hosting

The site is served from Cloudflare Workers static assets at <https://tiktok-shop-api.docs.isaackogan.com/>. `wrangler.jsonc` in this directory declares the asset directory and the custom domain; there is no Worker script. The GitHub workflow validates every change and deploys pushes to `main` when the repository has the `CLOUDFLARE_API_TOKEN` and `CLOUDFLARE_ACCOUNT_ID` secrets.

To deploy from a checkout after the install above:

```sh
pnpm --dir docs build
pnpm --dir docs run deploy:cloudflare
```

See [Cloudflare Workers hosting](src/content/docs/hosting.md) for the configuration, secrets, and verification steps. `DOCS_SITE` defaults to the custom domain and `DOCS_BASE` to `/`; neither needs to be set.
