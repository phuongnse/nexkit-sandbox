import unittest

from stats import mean, median, mode, spread, variance


class StatsTests(unittest.TestCase):
    def test_mean(self):
        self.assertEqual(mean([1, 2, 3, 4]), 2.5)

    def test_mean_empty(self):
        with self.assertRaises(ValueError) as ctx:
            mean([])
        self.assertIn("empty", str(ctx.exception))

    def test_median_odd(self):
        self.assertEqual(median([3, 1, 2]), 2)

    def test_median_even(self):
        self.assertEqual(median([1, 2, 3, 4]), 2.5)

    def test_median_empty(self):
        with self.assertRaises(ValueError):
            median([])

    def test_mode(self):
        self.assertEqual(mode([1, 2, 2, 3]), 2)

    def test_mode_tie_returns_smallest(self):
        self.assertEqual(mode([3, 1, 3, 1]), 1)

    def test_mode_empty(self):
        with self.assertRaises(ValueError) as ctx:
            mode([])
        self.assertIn("empty", str(ctx.exception))

    def test_spread(self):
        self.assertEqual(spread([1, 5, 3]), 4)

    def test_spread_single_value(self):
        self.assertEqual(spread([2]), 0)

    def test_spread_empty(self):
        with self.assertRaises(ValueError) as ctx:
            spread([])
        self.assertIn("empty", str(ctx.exception))

    def test_variance(self):
        self.assertEqual(variance([1, 2, 3, 4]), 1.25)

    def test_variance_empty(self):
        with self.assertRaises(ValueError) as ctx:
            variance([])
        self.assertIn("empty", str(ctx.exception))


if __name__ == "__main__":
    unittest.main()
