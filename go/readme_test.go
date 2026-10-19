package tiktokshop_test

import (
	"os"
	"regexp"
	"strings"
	"testing"
)

// TestREADMEMatchesExamples fails when a line of a README ```go block is missing from
// example_readme_test.go, which the compiler builds. Imports count: each block's import lines must be
// in the file's import group.
func TestREADMEMatchesExamples(t *testing.T) {
	readme, err := os.ReadFile("README.md")
	if err != nil {
		t.Fatal(err)
	}
	src, err := os.ReadFile("example_readme_test.go")
	if err != nil {
		t.Fatal(err)
	}
	have := map[string]bool{}
	for _, l := range strings.Split(string(src), "\n") {
		have[strings.TrimSpace(l)] = true
	}
	blocks := regexp.MustCompile("(?s)```go\n(.*?)```").FindAllStringSubmatch(string(readme), -1)
	if len(blocks) < 5 {
		t.Fatalf("expected at least 5 go blocks in the README, found %d", len(blocks))
	}
	for i, b := range blocks {
		if !strings.Contains(b[1], "import (") {
			t.Errorf("block %d has no imports of its own", i+1)
		}
		for _, l := range strings.Split(b[1], "\n") {
			if l = strings.TrimSpace(l); l != "" && !have[l] {
				t.Errorf("block %d: README line %q is not in example_readme_test.go", i+1, l)
			}
		}
	}
}
