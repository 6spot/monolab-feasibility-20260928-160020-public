"""A pure farewell helper.

This module exposes a single pure function, :func:`farewell`, that formats
a goodbye message for a given name. It performs no filesystem or network
I/O and uses only the Python standard library.
"""


def farewell(name: str) -> str:
    """Return a goodbye message for *name*.

    Surrounding whitespace is trimmed from *name* first. If the trimmed
    name is nonempty, the result is ``"Goodbye, <name>!"`` using the
    trimmed name. If the trimmed name is blank (empty or whitespace-only),
    the result is ``"Goodbye, friend!"``.

    Unicode characters in *name* are preserved exactly; no transliteration,
    ASCII folding or encoding changes are performed.
    """
    trimmed = name.strip()
    if trimmed:
        return f"Goodbye, {trimmed}!"
    return "Goodbye, friend!"
