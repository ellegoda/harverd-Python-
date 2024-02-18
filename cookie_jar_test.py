import unittest
from jar import Jar


class TestJar(unittest.TestCase):

    def test_initialization(self):
        jar = Jar()
        self.assertEqual(jar.capacity, 12)
        self.assertEqual(jar.size, 0)

        custom_capacity = 20
        jar_custom = Jar(custom_capacity)
        self.assertEqual(jar_custom.capacity, custom_capacity)
        self.assertEqual(jar_custom.size, 0)

    def test_deposit(self):
        jar = Jar()

        jar.deposit(5)
        self.assertEqual(jar.size, 5)

        with self.assertRaises(ValueError):
            jar.deposit(8)

        with self.assertRaises(ValueError):
            jar.deposit(-3)

        with self.assertRaises(ValueError):
            jar.deposit("abc")

    def test_withdraw(self):
        jar = Jar()

        jar.deposit(8)

        jar.withdraw(3)
        self.assertEqual(jar.size, 5)

        with self.assertRaises(ValueError):
            jar.withdraw(7)

        with self.assertRaises(ValueError):
            jar.withdraw(-2)

        with self.assertRaises(ValueError):
            jar.withdraw("xyz")

    def test_str_representation(self):
        jar = Jar()

        jar.deposit(5)

        self.assertEqual(str(jar), "🍪🍪🍪🍪🍪")


if __name__ == '__main__':
    unittest.main()
