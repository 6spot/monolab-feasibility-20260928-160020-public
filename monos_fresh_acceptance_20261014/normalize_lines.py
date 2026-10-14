"""Line normalization module for the monos_fresh_acceptance_20261014 deliverable.

Exposes :func:`normalize_lines`, a pure function built only on the
Python 3 standard library with no network or filesystem side effects.
"""


def normalize_lines(text: str) -> list[str]:
    """Return a normalized list of lines from ``text``.

    The input is split into lines (LF, CRLF, or lone CR line endings
    are all handled), surrounding whitespace is trimmed from each line,
    blank (post-trim) lines are discarded, exact case-sensitive
    duplicates are removed, and first-occurrence order is preserved.

    Only the Python 3 standard library is used.
    """
    seen = set()
    normalized = []
    for raw_line in text.splitlines():
        line = raw_line.strip()
        if not line:
            continue
        if line in seen:
            continue
        seen.add(line)
        normalized.append(line)
    return normalized
