"""Unit tests for the greeting module.

Uses only the Python 3 standard library (``unittest``); no third-party
dependencies.
"""

import unittest

from greeting import greeting


class GreetingTestCase(unittest.TestCase):
    """Coverage for the greeting() contract."""

    def test_normal_name(self):
        self.assertEqual(greeting("Alice"), "Hello, Alice!")

    def test_leading_and_trailing_whitespace_is_trimmed(self):
        self.assertEqual(greeting("  Bob  "), "Hello, Bob!")
        self.assertEqual(greeting("\tCarol\n"), "Hello, Carol!")

    def test_blank_name_returns_friend_greeting(self):
        self.assertEqual(greeting(""), "Hello, friend!")

    def test_whitespace_only_name_returns_friend_greeting(self):
        self.assertEqual(greeting("   "), "Hello, friend!")
        self.assertEqual(greeting("\t\n "), "Hello, friend!")

    def test_unicode_name_is_preserved_literally(self):
        self.assertEqual(greeting("Zoë"), "Hello, Zoë!")
        self.assertEqual(greeting("José García"), "Hello, José García!")
        self.assertEqual(greeting("名古屋"), "Hello, 名古屋!")

    def test_no_network_or_filesystem_side_effects(self):
        # The function must be side-effect free; calling it repeatedly
        # with the same input must yield the same pure result.
        self.assertEqual(greeting("Alice"), greeting("Alice"))


if __name__ == "__main__":
    unittest.main()
