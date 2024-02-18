import unittest
from seasons import ageInminutes

class TestseasonsValidation(unittest.TestCase):
    def test_birthdate(self):
        self.assertEqual(ageInminutes('1999-01-01'), "Thirteen million, two hundred fourteen thousand, eight hundred eighty minutes")

    def test_date_two_years_ago_from_today(self):
        self.assertEqual(ageInminutes('2022-02-16'), "One million, fifty-one thousand, two hundred minutes")

    def test_invalid_date(self):
        with self.assertRaises(SystemExit) as cm:
            ageInminutes('February 6th, 1998')

        self.assertEqual(cm.exception.code, 1)
