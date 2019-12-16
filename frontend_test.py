import unittest
from frontend import Frontend


class TestFrontend(unittest.TestCase):

    def setUp(self):
        self.fe = Frontend()

    def test_wpm_coloring(self):
        white = 255, 255, 255
        green = 0, 255, 0
        yellow = 255, 255, 0
        red = 255, 0, 0
        self.assertEqual(self.fe.wpm_coloring(0), white)
        self.assertEqual(self.fe.wpm_coloring(29), green)
        self.assertEqual(self.fe.wpm_coloring(30), yellow)
        self.assertEqual(self.fe.wpm_coloring(60), red)


if __name__ == '__main__':
    unittest.main()
