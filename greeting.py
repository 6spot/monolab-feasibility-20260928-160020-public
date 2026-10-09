"""Greeting module for the monolab feasibility repository.

Exposes :func:`greeting`, a pure function with no network or filesystem
side effects.
"""


def greeting(name: str) -> str:
    """Return a greeting for ``name``, preserving the name literally.

    Leading and trailing whitespace is stripped from ``name``.  If the
    stripped result is nonempty, it is substituted literally into
    ``"Hello, <name>!"``.  If the stripped result is empty or
    whitespace-only, ``"Hello, friend!"`` is returned instead.  Unicode
    names are preserved as literal text: no normalization, encoding
    conversion, or transliteration is applied.
    """
    stripped = name.strip()
    if not stripped:
        return "Hello, friend!"
    return "Hello, {}!".format(stripped)
