import unittest
from r_lib.data_utils import convert_to_int

class TestDataUtils(unittest.TestCase):
    def test_convert_to_int(self):
        self.assertEqual(convert_to_int("10"), 10)
        self.assertEqual(convert_to_int("-5"), -5)
        self.assertEqual(convert_to_int("abc"), None)
        self.assertEqual(convert_to_int(3.7), 3)

if __name__ == "__main__":
    unittest.main()