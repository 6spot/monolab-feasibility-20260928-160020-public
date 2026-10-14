"""Unit tests for the normalize_lines module.

Uses only the Python 3 standard library (``unittest``); no third-party
dependencies.
"""

import unittest

from normalize_lines import normalize_lines


class NormalizeLinesTestCase(unittest.TestCase):
    """Coverage for the normalize_lines() contract."""

    def test_empty_input(self):
        self.assertEqual(normalize_lines(""), [])

    def test_whitespace_only_input(self):
        self.assertEqual(normalize_lines("   \n\t\n  "), [])
        self.assertEqual(normalize_lines("\n\n\n"), [])

    def test_single_line_input(self):
        self.assertEqual(normalize_lines("  only one line  "), ["only one line"])

    def test_surrounding_whitespace_is_trimmed(self):
        self.assertEqual(
            normalize_lines("  alpha  \n\tbeta\t\n  gamma "),
            ["alpha", "beta", "gamma"],
        )

    def test_blank_lines_are_discarded(self):
        self.assertEqual(
            normalize_lines("one\n\n  \n\t\ntwo\n\nthree"),
            ["one", "two", "three"],
        )

    def test_duplicate_removal_preserves_first_occurrence_order(self):
        self.assertEqual(
            normalize_lines("alpha\nbeta\nalpha\ngamma\nbeta"),
            ["alpha", "beta", "gamma"],
        )

    def test_duplicates_after_trimming_are_removed(self):
        # "  alpha  " and " alpha " both trim to "alpha"; only the first
        # occurrence is kept.
        self.assertEqual(
            normalize_lines("alpha\n  alpha  \nbeta\n alpha "),
            ["alpha", "beta"],
        )

    def test_mixed_crlf_and_lf_line_endings(self):
        self.assertEqual(
            normalize_lines("one\r\ntwo\nthree\r\nfour\nfive"),
            ["one", "two", "three", "four", "five"],
        )

    def test_lone_carriage_return_line_endings(self):
        self.assertEqual(normalize_lines("one\rtwo\rthree"), ["one", "two", "three"])

    def test_case_sensitive_distinct_values_are_kept(self):
        # "Foo", "foo", and "FOO" are exact, case-sensitive distinct
        # values, so all are kept even when duplicated.
        self.assertEqual(
            normalize_lines("Foo\nfoo\nFOO\nfoo\nFoo"),
            ["Foo", "foo", "FOO"],
        )


if __name__ == "__main__":
    unittest.main()
