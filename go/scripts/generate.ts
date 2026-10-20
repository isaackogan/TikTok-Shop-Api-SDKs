import { execFileSync } from 'node:child_process';
import { cpSync, existsSync, mkdirSync, readdirSync, readFileSync, rmSync, writeFileSync } from 'node:fs';
import { resolve } from 'node:path';
import { renderMeta } from './render-meta.ts';
import { fixDecodeErrors, DECODE_ERROR_GO } from './fix-decode.ts';

const pkg = resolve(import.meta.dirname, '..');
const root = resolve(pkg, '..');
const run = (cmd: string, args: string[], cwd = root) => execFileSync(cmd, args, { cwd, stdio: 'inherit' });

run('pnpm', ['exec', 'tsx', 'scripts/prepare-spec.ts', '--lang', 'go']);

const out = resolve(pkg, 'build/_out');
rmSync(out, { recursive: true, force: true });
run('pnpm', [
  'exec', 'openapi-generator-cli', 'generate',
  '-g', 'go',
  '-i', 'go/build/openapi.json',
  '-o', 'go/build/_out',
  '--global-property', 'apiDocs=false,modelDocs=false,apiTests=false,modelTests=false',
  '--additional-properties=packageName=generated,enumClassPrefix=true,withGoMod=false,disallowAdditionalPropertiesIfNotPresent=false',
  // The spec has a schema called Time, which collides with time.Time's usual import name.
  '--model-name-mappings=Time=TimeInfo',
]);

// (build/_out: the leading underscore keeps the go tool from compiling or vetting it.)
// Only the Go sources: the generator's README, docs, git_push.sh and api/ are discarded.
const dest = resolve(pkg, 'generated');
rmSync(dest, { recursive: true, force: true });
mkdirSync(dest, { recursive: true });
for (const f of readdirSync(out).filter((n) => n.endsWith('.go'))) cpSync(resolve(out, f), resolve(dest, f));

// The generated WebhookEvent oneOf union is never used (webhooks.go dispatches on `type` itself) and its
// unmarshaller has unreachable code that fails `go vet`, so it is not shipped. Asserted: a rename fails loudly.
const union = resolve(dest, 'model_webhook_event.go');
if (!existsSync(union)) throw new Error('fix-up: generated/model_webhook_event.go (the WebhookEvent union) was not generated');
rmSync(union);

// R13d: a 2xx body that does not decode into its model returns generated.DecodeError(...), which the tiktokshop
// package sets to build a *tiktokshop.Error, instead of a *GenericOpenAPIError. Asserted per file.
for (const f of readdirSync(dest).filter((n) => /^api_.*\.go$/.test(n))) {
  const path = resolve(dest, f);
  writeFileSync(path, fixDecodeErrors(readFileSync(path, 'utf8'), f));
}
writeFileSync(resolve(dest, 'decode_error.go'), DECODE_ERROR_GO);

renderMeta(resolve(pkg, 'build/meta.json'), dest, resolve(pkg, 'build/openapi.json'));
run('gofmt', ['-w', 'generated/meta.go', 'generated/webhook_models.go', 'generated/webhook_required.go', 'generated/decode_error.go'], pkg);
