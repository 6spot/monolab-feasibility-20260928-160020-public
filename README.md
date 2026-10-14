# monolab-feasibility-20260928-160020-public
Synthetic MonoLab provider feasibility fixture; no product source.

## greeting module

`greeting.py` at the repository root exposes `greeting(name: str) -> str`:

- Leading and trailing whitespace is stripped from `name`.
- A nonempty stripped name is substituted literally: `Hello, <name>!`.
- A blank or whitespace-only name produces `Hello, friend!`.
- Unicode names are preserved literally (no normalization, encoding
  conversion, or transliteration).

The function is pure: it performs no network or filesystem access.

Tests live in `tests/test_greeting.py` and use only the Python 3 standard
library (`unittest`). Run them from the repository root with:

```
python3 -m unittest discover -s tests -v
```

## normalize_lines module

`monos_fresh_acceptance_20261014/normalize_lines.py` exposes
`normalize_lines(text: str) -> list[str]`:

- The input is split into lines (LF, CRLF, and lone CR endings handled).
- Surrounding whitespace is trimmed from each line.
- Blank (post-trim) lines are discarded.
- Exact case-sensitive duplicates are removed, preserving first-occurrence order.

The function is pure and uses only the Python 3 standard library.

Tests live in `monos_fresh_acceptance_20261014/test_normalize_lines.py`
and use only the Python 3 standard library (`unittest`). Run them from
the repository root with:

```
python3 -m unittest discover -s monos_fresh_acceptance_20261014 -v
```

Edge coverage includes empty and whitespace-only input, blank-line
removal, Unicode non-breaking spaces (U+00A0, U+3000) mixed with tabs
around line content, duplicates separated by blank lines, preservation
of internal whitespace, mixed CRLF/LF and lone-CR line endings, and
case-sensitive distinct values. The suite runs 13 tests, all passing.
