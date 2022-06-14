import unittest

class TruthyAndFalsyTest(unittest.TestCase):
    def test_tuthiness(self):
        self.assertTrue(3 < 5)
        
    def test_falsyness(self):
        self.assertFalse(5 < 3)

if __name__ == "__main__":
    unittest.main()