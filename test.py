import unittest
import example


class TestCase(unittest.TestCase):
    def test_add_1(self):
        self.assertEqual(example.add(1, 2), 3)

    def test_sub_1(self):
        self.assertEqual(example.sub(1, 1), 0)

    def test_mul_1(self):
        self.assertEqual(example.mul(2, 5), 10)


if __name__ == '__main__':
    unittest.main()
