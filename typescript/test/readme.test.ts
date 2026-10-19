import { readFileSync } from 'node:fs';
import { expect, it } from 'vitest';

it('test/readme-examples.ts contains every statement of the README ts blocks', () => {
  const readme = readFileSync(new URL('../README.md', import.meta.url), 'utf8');
  const file = readFileSync(new URL('./readme-examples.ts', import.meta.url), 'utf8').split('\n').map((l) => l.trim());
  const blocks = [...readme.matchAll(/```ts\n([\s\S]*?)```/g)].map((m) => m[1]!);
  expect(blocks.length).toBe(4);
  for (const line of blocks.flatMap((b) => b.split('\n')).map((l) => l.trim()).filter((l) => l && !l.startsWith('import '))) {
    expect(file, line).toContain(line);
  }
});
