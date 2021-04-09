import unittest

from our_library import our_add


class TestAdd(unittest.TestCase):
    def test_basic(self):
        """Test that it can add up two numbers"""
        result = our_add(30, 50)
        self.assertEqual(80, result)

    def test_negative(self):
        result = our_add(-50, 150)
        self.assertEqual(100, result)

    def test_both_negative(self):
        result = our_add(-150, -1150)
        self.assertEqual(-1300, result)

    def test_large_number(self):
        result = our_add(10_000_000, 10)
        self.assertEqual(10_000_010, result)

    def test_both_large(self):
        result = our_add(300_000_000, 256_000_000)
        self.assertEqual(556_000_000, result)

    def test_large_negative(self):
        result = our_add(-300_000_000, 252_592_038)
        self.assertEqual(-47_407_962, result)

    def test_both_large_negative(self):
        result = our_add(-211_502_300, -349_932_558)
        self.assertEqual(-561_434_858, result)


if __name__ == '__main__':
    unittest.main()
