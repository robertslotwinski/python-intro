import unittest
from r_lib.text_processing import reverse_text, count_vowels

class TestTextProcessing(unittest.TestCase):
    def test_reverse_text(self):
        self.assertEqual(reverse_text("hello"), "olleh")
        self.assertEqual(reverse_text("Python"), "nohtyP")
    
    def test_count_vowels(self):
        self.assertEqual(count_vowels("hello"), 2)
        self.assertEqual(count_vowels("PYTHON"), 1)
        self.assertEqual(count_vowels("bcdfg"), 0)

if __name__ == "__main__":
    unittest.main()