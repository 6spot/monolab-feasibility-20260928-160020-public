"""Unit tests for the greeting module.

Uses only the Python 3 standard library (``unittest``); no third-party
dependencies.
"""

import builtins
import socket
import unittest

from greeting import greeting


class GreetingTestCase(unittest.TestCase):
    """Coverage for the greeting() contract."""

    def test_normal_name(self):
        self.assertEqual(greeting("Alice"), "Hello, Alice!")

    def test_leading_and_trailing_whitespace_is_trimmed(self):
        self.assertEqual(greeting("  Bob  "), "Hello, Bob!")
        self.assertEqual(greeting("\tCarol\n"), "Hello, Carol!")

    def test_unicode_surrounding_whitespace_is_trimmed(self):
        # U+00A0 (no-break space) and U+3000 (ideographic space) are
        # stripped like ASCII whitespace while the Unicode name itself is
        # preserved literally.
        self.assertEqual(greeting("\u00a0Zoë\u00a0"), "Hello, Zoë!")
        self.assertEqual(greeting("\u3000名古屋\u3000"), "Hello, 名古屋!")

    def test_blank_name_returns_friend_greeting(self):
        self.assertEqual(greeting(""), "Hello, friend!")

    def test_whitespace_only_name_returns_friend_greeting(self):
        self.assertEqual(greeting("   "), "Hello, friend!")
        self.assertEqual(greeting("\t\n "), "Hello, friend!")
        self.assertEqual(greeting("\u00a0\u3000"), "Hello, friend!")

    def test_unicode_name_is_preserved_literally(self):
        self.assertEqual(greeting("Zoë"), "Hello, Zoë!")
        self.assertEqual(greeting("José García"), "Hello, José García!")
        self.assertEqual(greeting("名古屋"), "Hello, 名古屋!")

    def test_decomposed_unicode_name_is_preserved_literally(self):
        # "José" in decomposed (NFD) form: 'e' + U+0301 combining acute
        # accent.  The exact code points must be preserved; greeting()
        # must not normalize them to the composed form.
        decomposed = "Jose\u0301"
        self.assertEqual(greeting(decomposed), "Hello, {}!".format(decomposed))
        self.assertNotEqual(greeting(decomposed), "Hello, José!")

    def test_no_network_or_filesystem_side_effects(self):
        # Meaningful no-I/O guard: swap the filesystem and network entry
        # points for functions that raise AssertionError.  If greeting()
        # attempted any filesystem or network I/O, the guard would fire
        # and this test would fail.
        real_open = builtins.open
        real_socket = socket.socket

        def guarded_open(*args, **kwargs):
            raise AssertionError("greeting() must not perform filesystem I/O")

        def guarded_socket(*args, **kwargs):
            raise AssertionError("greeting() must not perform network I/O")

        builtins.open = guarded_open
        socket.socket = guarded_socket
        try:
            self.assertEqual(greeting("Alice"), "Hello, Alice!")
            self.assertEqual(greeting("  \t "), "Hello, friend!")
            self.assertEqual(greeting("名古屋"), "Hello, 名古屋!")
        finally:
            builtins.open = real_open
            socket.socket = real_socket


if __name__ == "__main__":
    unittest.main()
