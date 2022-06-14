import unittest

class TestInequality(unittest.TestCase):
    def test_inequality(self):
        self.assertNotEqual(1, 2)
        self.assertNotEqual(True, False)
        self.assertNotEqual("Hello", "hello")


if __name__== "__main__":
    unittest.main()