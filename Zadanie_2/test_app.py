import unittest
from app import *

class TestAppFunctions(unittest.TestCase):

    def test_is_valid_email(self):
        # poprawne
        self.assertTrue(is_valid_email("john.doe@gmail.com"))
        self.assertTrue(is_valid_email("a@b.pl"))
        # błędne
        self.assertFalse(is_valid_email("user@domain"))
        self.assertFalse(is_valid_email("@domain.com"))
        self.assertFalse(is_valid_email("user@domain.c"))
        self.assertFalse(is_valid_email("user@.com"))
        self.assertFalse(is_valid_email("user@@domain.com"))

    def test_calculate_rectangle_area(self):
        self.assertEqual(calculate_rectangle_area(3, 4), 12)
        self.assertEqual(calculate_rectangle_area(0, 5), 0)
        with self.assertRaises(ValueError):
            calculate_rectangle_area(-3, 4)

    def test_filter_even_numbers(self):
        self.assertEqual(filter_even_numbers([1, 2, 3, 4]), [2, 4])
        self.assertEqual(filter_even_numbers([1, 3, 5]), [])
        self.assertEqual(filter_even_numbers([]), [])
        self.assertEqual(filter_even_numbers([2, '4', 6]), [2, 6])  

    def test_convert_date_format(self):
        self.assertEqual(convert_date_format("01-01-2000"), "2000/01/01")
        self.assertEqual(convert_date_format("21-03-2024"), "2024/03/21")
        with self.assertRaises(ValueError):
            convert_date_format("2024-03-21")
        with self.assertRaises(ValueError):
            convert_date_format("invalid-date")

    def test_is_palindrome(self):
        self.assertTrue(is_palindrome("Kajak"))
        self.assertTrue(is_palindrome("A man, a plan, a canal: Panama"))
        self.assertFalse(is_palindrome("Hello World!"))
        self.assertTrue(is_palindrome(""))

if __name__ == '__main__':
    unittest.main()
