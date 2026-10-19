import re
from pathlib import Path


def test_readme_examples_module_contains_every_statement_of_the_readme_python_blocks():
    readme = (Path(__file__).parents[1] / "README.md").read_text()
    module = [l.strip() for l in (Path(__file__).parent / "readme_examples.py").read_text().splitlines()]
    blocks = re.findall(r"```python\n(.*?)```", readme, re.S)
    assert len(blocks) == 5
    for block in blocks:
        for line in (l.strip() for l in block.splitlines()):
            if line and not line.startswith(("import ", "from ", ")")):
                assert line in module, line


def test_readme_examples_import_without_network():
    import readme_examples  # noqa: F401  (needs tests/ on sys.path; pytest's rootdir insertion provides it)
