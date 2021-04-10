import unittest

from TedovaKnihovna import *

# TODO  add tests with flots to our_add
# TODO  add tests for other methods
# TODO  find out how to import the entire library properly

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

    def test_float_small(self):
        result = our_add(0.5, 0.5)
        self.assertEqual(1, result)

    def test_float_negative(self):
        result = our_add(-0.02, - 0.005)
        self.assertEqual(-0.025, result)


class testSub(unittest.TestCase):
    def test_small_nums(self):
        result = our_sub(10, 30)
        self.assertEqual(40, result)

    def test_big_nums(self):
        result = our_sub(30_000_000, 10_000_000)
        self.assertEqual(20_000_000, result)

    def test_small_negative(self):
        result = our_sub(-340, -200)
        self.assertEqual(-140, result)

    def test_large_negative(self):
        result = our_sub(-20_000_000, 10_000_000)
        self.assertEqual(-30_000_000, result)

    def test_float_small(self):
        result = our_sub(0.002, 0.001)
        self.assertEqual(0.001, result)

    def test_float_large(self):
        result = our_sub(50_000.7, 30_000.5)
        self.assertEqual(20_000.2, result)

class testMul(unittest.TestCase):
    def test_small_nums(self):
        result = our_mul(10, 30)
        self.assertEqual(300, result)

    def test_big_nums(self):
        result = our_mul(30_000, 10_000_000)
        self.assertEqual(300_000_000_000, result)

    def test_small_negative(self):
        result = our_mul(-340, -200)
        self.assertEqual(68_000, result)

    def test_large_negative(self):
        result = our_mul(-20_000_000, 1000)
        self.assertEqual(-20_000_000_000, result)

    def test_float_small(self):
        result = our_mul(0.002, 0.001)
        self.assertEqual(0.000002, result)

    def test_float_large(self):
        result = our_mul(50_000.7, 30_000.5)
        self.assertEqual(1_500_046_000,35, result)


if __name__ == '__main__':
    unittest.main()