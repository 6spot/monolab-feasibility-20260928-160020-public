"""Standard-library unittest tests for the farewell module."""

import unittest

import farewell


class FarewellTests(unittest.TestCase):
    """Tests for farewell.farewell."""

    def test_nonempty_name(self):
        self.assertEqual(farewell.farewell("Ada"), "Goodbye, Ada!")

    def test_empty_name_returns_friend(self):
        self.assertEqual(farewell.farewell(""), "Goodbye, friend!")

    def test_whitespace_only_name_returns_friend(self):
        self.assertEqual(farewell.farewell("   \t\n  "), "Goodbye, friend!")

    def test_surrounding_whitespace_is_trimmed(self):
        self.assertEqual(farewell.farewell("  Grace  "), "Goodbye, Grace!")

    def test_unicode_characters_are_preserved(self):
        name = "Jörg Müller 🎉"
        self.assertEqual(farewell.farewell(name), f"Goodbye, {name}!")

    def test_inner_whitespace_is_preserved(self):
        self.assertEqual(
            farewell.farewell("  Marie  Curie  "), "Goodbye, Marie  Curie!"
        )


if __name__ == "__main__":
    unittest.main()
