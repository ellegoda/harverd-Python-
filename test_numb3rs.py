import unittest
from numb3rs import validate


class TestNumb3rs(unittest.TestCase):

    def test_valid_ipv4(self):
        self.assertTrue(validate("192.168.0.1"))
        self.assertTrue(validate("255.255.255.255"))

    def test_invalid_ipv4(self):
        self.assertFalse(validate("256.0.0.1"))
        self.assertFalse(validate("192.168.0.300"))
        self.assertFalse(validate("192.168.0"))
        self.assertFalse(validate("192.168.0.1.2"))
        self.assertFalse(validate("192.168.0.-1"))
        self.assertTrue(validate("192.168.0.01"))

    def test_malformed_ipv4(self):
        self.assertFalse(validate("192.168.0"))
        self.assertFalse(validate("192.168.0.1.2"))
        self.assertFalse(validate("192.168.0.-1"))
        self.assertTrue(validate("192.168.0.01"))

    def test_empty_input(self):
        self.assertFalse(validate(""))


if __name__ == "__main__":
    unittest.main()
