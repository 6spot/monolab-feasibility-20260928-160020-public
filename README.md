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
