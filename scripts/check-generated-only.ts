import { execFileSync } from 'node:child_process';
import { fileURLToPath } from 'node:url';

const GENERATED = [
  'typescript/src/generated/',
  'python/src/tiktok_shop_api/generated/',
  'go/generated/',
  'java/src/main/java/com/isaackogan/tiktok/shop/generated/',
  'kotlin/src/main/kotlin/com/isaackogan/tiktok/shop/generated/',
  'php/src/Generated/',
  'rust/src/generated/',
  'csharp/src/TikTokShop.Api/Generated/',
];
const LANGS = ['typescript', 'python', 'go', 'java', 'kotlin', 'php', 'rust', 'csharp'];
const ALLOWED = [...GENERATED, ...LANGS.map((l) => `${l}/build/`)];

function allowed(path: string): boolean {
  if (path.split('/').includes('..')) return false;
  return ALLOWED.some((p) => path.startsWith(p));
}

// Undo git's C-style quoting ("..." with \" \\ \n \t and octal bytes).
function unquote(p: string): string {
  if (p.length < 2 || !p.startsWith('"') || !p.endsWith('"')) return p;
  const bytes: number[] = [];
  const s = p.slice(1, -1);
  for (let i = 0; i < s.length; i++) {
    if (s[i] !== '\\') {
      bytes.push(...Buffer.from(s[i], 'utf8'));
      continue;
    }
    const n = s[++i];
    if (/[0-7]/.test(n)) {
      const oct = s.slice(i, i + 3);
      bytes.push(parseInt(oct, 8));
      i += oct.length - 1;
    } else {
      const map: Record<string, string> = { n: '\n', t: '\t', r: '\r', a: '\x07', b: '\b', f: '\f', v: '\v' };
      bytes.push(...Buffer.from(map[n] ?? n, 'utf8'));
    }
  }
  return Buffer.from(bytes).toString('utf8');
}

/** Paths in `git status --porcelain` (v1, newline or -z form) outside every allowed folder. */
export function offendingPaths(porcelain: string): string[] {
  const touched: string[] = [];
  if (porcelain.includes('\0')) {
    const toks = porcelain.split('\0').filter((t) => t !== '');
    for (let i = 0; i < toks.length; i++) {
      const status = toks[i].slice(0, 2);
      touched.push(toks[i].slice(3));
      if (/[RC]/.test(status)) touched.push(toks[++i] ?? ''); // -z: new path first, then old
    }
  } else {
    for (const line of porcelain.split('\n')) {
      if (line.trim() === '') continue;
      const rest = line.slice(3);
      if (/[RC]/.test(line.slice(0, 2)) && rest.includes(' -> ')) {
        const i = rest.indexOf(' -> ');
        touched.push(unquote(rest.slice(0, i)), unquote(rest.slice(i + 4)));
      } else {
        touched.push(unquote(rest));
      }
    }
  }
  return touched.filter((p) => p !== '' && !allowed(p));
}

/** Raw `git status` output; the buffer is large because -uall lists every generated file. */
export function readPorcelain(cwd: string): string {
  return execFileSync('git', ['status', '--porcelain', '-z', '-uall'], {
    cwd,
    encoding: 'utf8',
    maxBuffer: 1024 * 1024 * 1024,
    
  });
}

if (process.argv[1] && fileURLToPath(import.meta.url) === process.argv[1]) {
  const root = fileURLToPath(new URL('../', import.meta.url));
  const bad = offendingPaths(readPorcelain(root));
  if (bad.length > 0) {
    console.error('Generation touched files outside the generated folders:');
    for (const p of bad) console.error(`  ${p}`);
    process.exit(1);
  }
  console.log('OK: only generated folders changed.');
}
