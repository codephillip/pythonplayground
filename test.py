import unittest
from main import renewal_calc, private_calc


class MyTestCase(unittest.TestCase):
    def test_calc(self):
        self.assertEqual(renewal_calc(50000, 2), 50000)
        self.assertEqual(renewal_calc(50000, 3), 75000)
        self.assertEqual(renewal_calc(50000, 5), 75000)
        self.assertEqual(renewal_calc(50000, 7), 150000)
        self.assertEqual(renewal_calc(80000, 0), 80000)
        self.assertEqual(renewal_calc(80000, 3), 120000)
        self.assertEqual(renewal_calc(80000, 5), 120000)
        self.assertEqual(renewal_calc(80000, 7), 240000)

        self.assertEqual(private_calc(50000, 0), 50000)
        self.assertEqual(private_calc(50000, 1), 75000)
        self.assertEqual(private_calc(50000, 2), 150000)


if __name__ == '__main__':
    unittest.main()
