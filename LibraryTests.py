import unittest

from TedovaKnihovna import * # just a placeholder so the intellisense doesnt scream at me for a wrong ref

# TODO  add tests for other methods
# TODO  find out how to import the entire library properly + change the lib name
# TODO  find out where using AlmostEqual instead of Equal is a good idea


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


class TestSub(unittest.TestCase):
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


class TestMul(unittest.TestCase):
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
        self.assertEqual(1_500_046_000.35, result)


class TestDiv(unittest.TestCase):
    def test_small_nums(self):
        result = our_div(50, 10)
        self.assertEqual(5, result)

    def test_big_nums(self):
        result = our_div(10_000_000, 50_000)
        self.assertEqual(200, result)

    def test_small_negative(self):
        result = our_div(-340, -20)
        self.assertEqual(17, result)

    def test_large_negative(self):
        result = our_div(-20_000_000, 1000)
        self.assertEqual(-20_000, result)

    def test_float_small(self):
        result = our_div(0.002, 0.001)
        self.assertEqual(2, result)

    def test_float_large(self):
        result = our_div(50_000.7, 30_000.5)
        self.assertAlmostEqual(1.6666622222962950617489708504858, result, 20)


class TestFact(unittest.TestCase):
    def test_small_num(self):
        result = our_fact(4)
        self.assertEqual(24, result)

    def test_zero(self):
        result = our_fact(0)
        self.assertEqual(1, result)

    def test_float(self):
        with self.assertRaises(Exception):
            our_fact(2.5)

    def test_negative(self):
        with self.assertRaises(Exception):
            our_fact(-10)


class TestPow(unittest.TestCase):
    def test_small_nums(self):
        result = our_pow(10, 3)
        self.assertEqual(1000, result)

    def test_large_nums(self):
        result = our_pow(10, 10)
        self.assertEqual(10_000_000_000, result)

    def test_small_negative(self):
        result = our_pow(-20, -2)
        self.assertAlmostEqual(0.0025, result, 20)

    def test_large_negative(self):
        result = our_pow(-100, 10)
        self.assertEqual(100_000_000_000_000_000_000, result)

    def test_float_small(self):
        result = our_pow(0.002, 0.001)
        self.assertAlmostEqual(0.99380466263779646744326432913976, result, 20)

    def test_float_large(self):
        result = our_pow(10.5, 3.4)
        self.assertAlmostEqual(2_965.129166883078114339313070216, result, 20)


class TestSqrt(unittest.TestCase):
    def test_small_nums(self):
        result = our_sqrt(2, 100)
        self.assertEqual(10, result)

    def test_large_nums(self):
        result = our_sqrt(3, 100_000_000)
        self.assertEqual(30_000, result)

    def test_small_negative(self):
        result = our_sqrt(-20, -2)
        self.assertAlmostEqual(0.0025, result, 20)

    def test_large_negative(self):
        result = our_sqrt(-100, 10)
        self.assertEqual(100_000_000_000_000_000_000, result)

    def test_float_small(self):
        result = our_sqrt(0.002, 0.001)
        self.assertAlmostEqual(0.99380466263779646744326432913976, result, 20)

    def test_float_large(self):
        result = our_sqrt(10.5, 3.4)
        self.assertAlmostEqual(2_965.129166883078114339313070216, result, 20)


if __name__ == '__main__':
    unittest.main()
