import { execFileSync } from 'node:child_process';
import { cpSync, existsSync, mkdirSync, rmSync, writeFileSync } from 'node:fs';
import { resolve } from 'node:path';
import { renderEvents } from './render-events.ts';
import { renderMeta } from './render-meta.ts';

const pkg = resolve(import.meta.dirname, '..');
const root = resolve(pkg, '..');
const run = (cmd: string, args: string[]) => execFileSync(cmd, args, { cwd: root, stdio: 'inherit' });

run('pnpm', ['exec', 'tsx', 'scripts/prepare-spec.ts', '--lang', 'csharp']);

const out = resolve(pkg, 'build/out');
rmSync(out, { recursive: true, force: true });

// Properties go in a config file (R20), not on the command line.
// R12: disallowAdditionalPropertiesIfNotPresent=false keeps unknown response fields from failing a decode.
const config = resolve(pkg, 'build/config.json');
writeFileSync(
  config,
  JSON.stringify({
    packageName: 'TikTokShop.Api.Generated',
    targetFramework: 'net8.0',
    nullableReferenceTypes: true,
    disallowAdditionalPropertiesIfNotPresent: false,
  }),
);
run('pnpm', [
  'exec', 'openapi-generator-cli', 'generate',
  '-g', 'csharp',
  '--library', 'httpclient',
  '-c', 'csharp/build/config.json',
  '-i', 'csharp/build/openapi.json',
  '-o', 'csharp/build/out',
  '--global-property', 'apiDocs=false,modelDocs=false,apiTests=false,modelTests=false',
]);

// Only Api, Client and Model: the generated csproj, README, docs and git_push.sh are discarded.
const src = resolve(out, 'src/TikTokShop.Api.Generated');
const dest = resolve(pkg, 'src/TikTokShop.Api/Generated');
rmSync(dest, { recursive: true, force: true });
mkdirSync(dest, { recursive: true });
for (const d of ['Api', 'Client', 'Model']) cpSync(resolve(src, d), resolve(dest, d), { recursive: true });

// The generated WebhookEvent oneOf union is never used (Webhooks.Parse dispatches on `type` itself) and its name would clash
// with the hand-written WebhookEvent base class, so it is not shipped.
const union = resolve(dest, 'Model/WebhookEvent.cs');
if (!existsSync(union)) throw new Error('expected the generated Model/WebhookEvent.cs, found none: the generator changed');
rmSync(union);

renderMeta(resolve(pkg, 'build/meta.json'), dest);
renderEvents(resolve(pkg, 'build/meta.json'), dest);
