import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';
import starlightOpenAPI, { openAPISidebarGroups } from 'starlight-openapi';
import starlightLinksValidator from 'starlight-links-validator';
import lucode from 'lucode-starlight';
import { visit } from 'unist-util-visit';
import { readFileSync } from 'node:fs';
import { unified } from '@astrojs/markdown-remark';
import { SDKS } from './sdks.mjs';
import { stampVersions } from './versions.mjs';

const base = `/${(process.env.DOCS_BASE || '').replace(/^\/+|\/+$/g, '')}/`.replace('//', '/');
const { info } = JSON.parse(readFileSync(new URL('../.openapi/tiktok-shop.openapi.json', import.meta.url), 'utf8'));
const repo = 'https://github.com/isaackogan/TikTok-Shop-Api-SDKs';

// starlight-openapi already includes the base in its links; authored Markdown does not.
function prefixLinks() {
  return (tree) => visit(tree, 'link', (node) => {
    if (node.url.startsWith('/') && !node.url.startsWith('//') && !node.url.startsWith(base)) {
      node.url = `${base}${node.url.slice(1)}`;
    }
  });
}

// Install snippets carry the released version; see versions.mjs.
function versionCode() {
  return (tree) => visit(tree, 'code', (node) => {
    node.value = stampVersions(node.value);
  });
}

export default defineConfig({
  site: process.env.DOCS_SITE || 'https://ttspa.docs.isaackogan.com',
  base,
  trailingSlash: 'always',
  markdown: { processor: unified({ remarkPlugins: [prefixLinks, versionCode] }) },
  integrations: [
    starlight({
      title: 'TikTok Shop Partner API',
      description: 'TikTok Shop Partner API docs: typed SDKs for TypeScript, Python, Go, Java, Kotlin, PHP, Rust and C#, and the OpenAPI spec they are generated from.',
      favicon: '/favicon.svg',
      social: [{ icon: 'github', label: 'GitHub', href: repo }],
      // Adds the "Unofficial Community SDKs" subtitle under the site title.
      customCss: ['./src/styles/custom.css'],
      editLink: { baseUrl: `${repo}/edit/main/docs/` },
      sidebar: [
        { label: 'Start here', items: [
          { label: 'Getting Started', slug: '' },
          { autogenerate: { directory: 'getting-started' } },
        ] },
        { label: 'SDKs', items: [
          { label: 'Choose an SDK', slug: 'sdks' },
          ...SDKS.map(({ dir, name }) => ({ label: name, items: [{ autogenerate: { directory: `sdks/${dir}` } }], collapsed: true })),
        ] },
        { label: 'OpenAPI', items: [
          { label: 'The spec', slug: 'openapi' },
          ...openAPISidebarGroups,
        ] },
        { label: 'Troubleshooting', slug: 'troubleshooting' },
        { label: 'Contributing to the docs', slug: 'contributing' },
        { label: 'Hosting', slug: 'hosting' },
      ],
      plugins: [lucode({
        navLinks: [
          { label: 'Docs', link: base },
          { label: 'SDKs', link: `${base}sdks/` },
          { label: 'API Reference', link: `${base}openapi/reference/` },
        ],
        footerText: `Unofficial project, not affiliated with or endorsed by TikTok or ByteDance. Generated from TikTok Shop's partner documentation (spec ${info.version}). Source on [GitHub](${repo}).`,
      }), starlightOpenAPI([{
        base: 'openapi/reference',
        schema: '../.openapi/tiktok-shop.openapi.json',
        sidebar: { label: 'API reference', collapsed: true, operations: { badges: true } },
        // Plain curl/fetch snippets would be unsigned requests TikTok rejects; the SDK pages show signed calls.
        snippets: { operation: false },
      }]), starlightLinksValidator({
        // The validator knows only authored pages: the reference root and the bundled spec files are generated.
        exclude: ['/openapi/reference/', '/openapi/tiktok-shop.openapi.json', '/openapi/tiktok-shop.openapi.yaml'],
      })],
    }),
  ],
});
