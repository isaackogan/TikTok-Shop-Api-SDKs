// Bundles the spec with the site: /openapi/tiktok-shop.openapi.{json,yaml} are served as downloads.
import { copyFile, mkdir } from 'node:fs/promises';

const from = new URL('../../.openapi/', import.meta.url);
const to = new URL('../public/openapi/', import.meta.url);
await mkdir(to, { recursive: true });
for (const name of ['tiktok-shop.openapi.json', 'tiktok-shop.openapi.yaml']) {
  await copyFile(new URL(name, from), new URL(name, to));
}
