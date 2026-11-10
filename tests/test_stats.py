import unittest

from stats import geometric_mean, harmonic_mean, mean, median, midrange, mode, spread, stdev, sum_of_squares, trimmed_mean, variance


class StatsTests(unittest.TestCase):
    def test_mean(self):
        self.assertEqual(mean([1, 2, 3, 4]), 2.5)

    def test_mean_empty(self):
        with self.assertRaises(ValueError) as ctx:
            mean([])
        self.assertIn("empty", str(ctx.exception))

    def test_mean_generator(self):
        self.assertEqual(mean(x for x in [1, 2, 3]), 2.0)

    def test_mean_empty_iterator(self):
        with self.assertRaises(ValueError) as ctx:
            mean(iter([]))
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

    def test_midrange(self):
        self.assertEqual(midrange([1, 5, 3]), 3.0)

    def test_midrange_single_value(self):
        self.assertEqual(midrange([2]), 2)

    def test_midrange_empty(self):
        with self.assertRaises(ValueError) as ctx:
            midrange([])
        self.assertIn("empty", str(ctx.exception))

    def test_stdev(self):
        self.assertEqual(stdev([2, 4, 4, 4, 5, 5, 7, 9]), 2.0)

    def test_stdev_empty(self):
        with self.assertRaises(ValueError) as ctx:
            stdev([])
        self.assertIn("empty", str(ctx.exception))

    def test_sum_of_squares(self):
        self.assertEqual(sum_of_squares([1, 2, 3]), 14)

    def test_sum_of_squares_negative(self):
        self.assertEqual(sum_of_squares([-2, 3]), 13)

    def test_sum_of_squares_empty(self):
        with self.assertRaises(ValueError) as ctx:
            sum_of_squares([])
        self.assertIn("empty", str(ctx.exception))

    def test_harmonic_mean(self):
        self.assertEqual(harmonic_mean([1, 4, 4]), 2.0)

    def test_harmonic_mean_empty(self):
        with self.assertRaises(ValueError) as ctx:
            harmonic_mean([])
        self.assertIn("empty", str(ctx.exception))

    def test_harmonic_mean_zero(self):
        with self.assertRaises(ValueError):
            harmonic_mean([1, 0])

    def test_harmonic_mean_negative(self):
        with self.assertRaises(ValueError):
            harmonic_mean([1, -2])

    def test_geometric_mean(self):
        self.assertAlmostEqual(geometric_mean([1, 4, 16]), 4.0)

    def test_geometric_mean_empty(self):
        with self.assertRaises(ValueError) as ctx:
            geometric_mean([])
        self.assertIn("empty", str(ctx.exception))

    def test_geometric_mean_not_positive(self):
        for bad in ([1, 0], [2, -3]):
            with self.assertRaises(ValueError):
                geometric_mean(bad)

    def test_trimmed_mean(self):
        self.assertEqual(trimmed_mean([1, 2, 3, 4, 100], 1), 3.0)
        self.assertEqual(trimmed_mean([1, 2, 3, 4], 0), 2.5)

    def test_trimmed_mean_empty(self):
        with self.assertRaises(ValueError) as ctx:
            trimmed_mean([], 0)
        self.assertIn("empty", str(ctx.exception))

    def test_trimmed_mean_nothing_left(self):
        for values, k in (([1, 2, 3, 4], 2), ([1, 2, 3], 2), ([1], 1)):
            with self.assertRaises(ValueError):
                trimmed_mean(values, k)

    def test_trimmed_mean_bad_k(self):
        for bad in (-1, 1.5, 1.0, True):
            with self.assertRaises(ValueError):
                trimmed_mean([1, 2, 3, 4, 5], bad)

    def test_trimmed_mean_unsorted_and_generator(self):
        self.assertEqual(trimmed_mean([100, 3, 1, 4, 2], 1), 3.0)
        self.assertEqual(trimmed_mean((x for x in [100, 3, 1, 4, 2]), 1), 3.0)


if __name__ == "__main__":
    unittest.main()
