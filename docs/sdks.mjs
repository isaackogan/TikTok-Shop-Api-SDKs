// The eight SDKs, in sidebar order. The sidebar, the SDK index and the content check all read this list.
export const SDKS = [
  { dir: 'typescript', name: 'TypeScript', fence: 'ts', readme: 'typescript/README.md' },
  { dir: 'python', name: 'Python', fence: 'python', readme: 'python/README.md' },
  { dir: 'go', name: 'Go', fence: 'go', readme: 'go/README.md' },
  { dir: 'java', name: 'Java', fence: 'java', readme: 'java/README.md' },
  { dir: 'kotlin', name: 'Kotlin', fence: 'kotlin', readme: 'kotlin/README.md' },
  { dir: 'php', name: 'PHP', fence: 'php', readme: 'php/README.md' },
  { dir: 'rust', name: 'Rust', fence: 'rust', readme: 'rust/README.md' },
  { dir: 'csharp', name: 'C#', fence: 'csharp', readme: 'csharp/README.md' },
];

// Every SDK section has these pages, in this order.
export const SDK_PAGES = ['index', 'authorization', 'calling-the-api', 'webhooks', 'errors'];
