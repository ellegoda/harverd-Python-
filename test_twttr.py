import unittest
from twttr import shorten


class TestTwttr(unittest.TestCase):

    def test_shorten_no_vowels(self):
        self.assertEqual(shorten("hello"), "hll")

    def test_shorten_all_vowels(self):
        self.assertEqual(shorten("AEIOUaeiou"), "")

    def test_shorten_mixed_case(self):
        self.assertEqual(shorten("Python"), "Pythn")

    def test_shorten_empty_string(self):
        self.assertEqual(shorten(""), "")

    def test_shorten_no_input(self):
        self.assertEqual(shorten(None), None)

    def test_shorten_special_characters(self):
        self.assertEqual(shorten("!@#$%^&*()"), "!@#$%^&*()")


if __name__ == '__main__':
    unittest.main()
