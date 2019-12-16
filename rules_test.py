import unittest
from rules import Rules


class TestRules(unittest.TestCase):

    def setUp(self):
        self.rule = Rules()

    def test_char_in_range(self):
        self.assertEqual(self.rule.char_in_range(), True)

    def test_word_in_range(self):
        self.assertEqual(self.rule.word_in_range(), True)


if __name__ == '__main__':
    unittest.main()
