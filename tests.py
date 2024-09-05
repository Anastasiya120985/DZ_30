import unittest
from DZ_30 import SetNum, Number


class TestSum(unittest.TestCase):
    def test_sum(self):
        f = SetNum(3, 4, 5, 8, 2, 9, 0)
        self.assertEqual(f.sum_val(), 31)

    def test_avg(self):
        f = SetNum(1, 2, 3, 4, 5, 6, 7, 8, 9)
        self.assertEqual(f.avg_val(), 5.0)

    def test_max(self):
        f = SetNum(3, 4, 5, 8, 2, 9, 0)
        self.assertEqual(f.max_val(), 9)

    def test_min(self):
        f = SetNum(3, 4, 5, 8, 2, 9, 0)
        self.assertEqual(f.min_val(), 0)


class TestNum(unittest.TestCase):
    def test_oct(self):
        f = Number(6)
        self.assertEqual(f.toOct(), '0o6')

    def test_hex(self):
        f = Number(7)
        self.assertEqual(f.toHex(), '0x7')

    def test_bin(self):
        f = Number(8)
        self.assertEqual(f.toBin(), '0b1000')


if __name__ == "__main__":
    unittest.main()