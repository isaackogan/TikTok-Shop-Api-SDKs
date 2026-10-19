import { execFileSync } from 'node:child_process';
import { cpSync, mkdirSync, readdirSync, rmSync } from 'node:fs';
import { resolve } from 'node:path';
import { renderMeta } from './render-meta.ts';

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
  '--additional-properties=packageName=generated,enumClassPrefix=true,withGoMod=false',
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
// unmarshaller has unreachable code that fails `go vet`, so it is not shipped.
rmSync(resolve(dest, 'model_webhook_event.go'), { force: true });

renderMeta(resolve(pkg, 'build/meta.json'), dest);
run('gofmt', ['-w', 'generated/meta.go', 'generated/webhook_models.go'], pkg);
