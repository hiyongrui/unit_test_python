import unittest
from pair import Pair

class PairTest(unittest.TestCase):
    def test_key(self):
        pair = Pair("a=b")
        self.assertEqual(pair.key, "a")
        self.assertEqual(pair.value, "b")

    def test_key_value(self):
        pair = Pair("a", "b")
        self.assertEqual(pair.key, "a")
        self.assertEqual(pair.value, "b")

    def test_invalid(self):
        with self.assertRaises(Exception) as context:
            pair = Pair("ab")
        self.assertEqual(str(context.exception), "Invalid pair.")

if __name__ == "__main__":
    unittest.main()
