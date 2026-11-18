import math
import unittest

from stats import coefficient_of_variation, contraharmonic_mean, count_above, cubic_mean, describe, geometric_mean, harmonic_mean, lehmer_mean, mean, mean_of_squares, median, midrange, mode, percentile, power_mean, quartic_mean, root_mean_square, spread, stdev, sum_of_squares, trimmed_mean, variance

class StatsTests(unittest.TestCase):
    def test_coefficient_of_variation(self):
        self.assertEqual(coefficient_of_variation([2, 4, 4, 4, 5, 5, 7, 9]), 0.4)

    def test_coefficient_of_variation_empty(self):
        with self.assertRaises(ValueError) as ctx:
            coefficient_of_variation([])
        self.assertIn("empty", str(ctx.exception))

    def test_coefficient_of_variation_zero_mean(self):
        for values in ([-1, 1], [0, 0]):
            with self.assertRaises(ValueError):
                coefficient_of_variation(values)

    def test_coefficient_of_variation_generator(self):
        self.assertEqual(coefficient_of_variation(x for x in [2, 4, 4, 4, 5, 5, 7, 9]), 0.4)

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

    def test_count_above(self):
        self.assertEqual(count_above([1, 5, 7], 4), 2)

    def test_count_above_empty(self):
        self.assertEqual(count_above([], 4), 0)

    def test_count_above_equal_not_counted(self):
        self.assertEqual(count_above([4, 4, 5], 4), 1)

    def test_count_above_generator(self):
        self.assertEqual(count_above((x for x in [1, 5, 7]), 4), 2)

    def test_percentile_90(self):
        self.assertAlmostEqual(percentile(list(range(1, 11)), 90), 9.1)

    def test_percentile_unsorted_equals_sorted(self):
        self.assertEqual(percentile([5, 1, 4, 2, 3], 30), percentile([1, 2, 3, 4, 5], 30))

    def test_percentile_single_value(self):
        self.assertEqual(percentile([7], 42), 7)

    def test_percentile_extremes(self):
        self.assertEqual(percentile([3, 9, 1], 0), 1)
        self.assertEqual(percentile([3, 9, 1], 100), 9)

    def test_percentile_median(self):
        self.assertEqual(percentile([4, 1, 3, 2], 50), median([4, 1, 3, 2]))

    def test_percentile_generator(self):
        self.assertAlmostEqual(percentile((x for x in range(1, 11)), 90), 9.1)

    def test_percentile_empty(self):
        with self.assertRaises(ValueError) as ctx:
            percentile([], 50)
        self.assertIn("empty", str(ctx.exception))

    def test_percentile_q_out_of_range(self):
        for q in (-1, 101, float("nan")):
            with self.assertRaises(ValueError):
                percentile([1, 2, 3], q)

    def test_describe(self):
        result = describe(list(range(1, 11)))
        self.assertEqual(result["count"], 10)
        self.assertAlmostEqual(result["mean"], 5.5)
        self.assertAlmostEqual(result["median"], 5.5)
        self.assertAlmostEqual(result["p90"], 9.1)

    def test_describe_empty(self):
        with self.assertRaises(ValueError) as ctx:
            describe([])
        self.assertIn("empty", str(ctx.exception))

    def test_describe_keys_and_stdev(self):
        values = [2, 4, 4, 4, 5, 5, 7, 9]
        result = describe(values)
        self.assertEqual(set(result), {"count", "mean", "median", "stdev", "p90"})
        self.assertEqual(result["stdev"], stdev(values))

    def test_describe_generator(self):
        self.assertEqual(describe(x for x in range(1, 11))["count"], 10)

    def test_root_mean_square_rule_d(self):
        self.assertAlmostEqual(root_mean_square([1, 1, 1]), 1.0)
        self.assertAlmostEqual(root_mean_square([3, 4]), math.sqrt(12.5))

    def test_root_mean_square_negative_rule_d(self):
        self.assertAlmostEqual(root_mean_square([-3, 4]), math.sqrt(12.5))

    def test_root_mean_square_generator_rule_d(self):
        self.assertAlmostEqual(root_mean_square(x for x in [3, 4]), math.sqrt(12.5))

    def test_root_mean_square_empty_rule_d(self):
        with self.assertRaises(ValueError) as ctx:
            root_mean_square([])
        self.assertEqual(str(ctx.exception), "root_mean_square() needs at least one value [L1]")

    def test_contraharmonic_mean_values_rule_d(self):
        self.assertAlmostEqual(contraharmonic_mean([1, 2, 3]), 14 / 6)
        self.assertAlmostEqual(contraharmonic_mean([2, 4]), 20 / 6)

    def test_contraharmonic_mean_empty_rule_d(self):
        with self.assertRaises(ValueError) as ctx:
            contraharmonic_mean([])
        self.assertEqual(str(ctx.exception), "contraharmonic_mean() needs at least one value [L1]")

    def test_lehmer_mean_values_rule_d(self):
        self.assertAlmostEqual(lehmer_mean([1, 2, 3], 2), contraharmonic_mean([1, 2, 3]))
        self.assertAlmostEqual(lehmer_mean([1, 2, 3], 1), mean([1, 2, 3]))
        self.assertAlmostEqual(lehmer_mean([1, 2, 3], 3), 36 / 14)

    def test_lehmer_mean_empty_rule_d(self):
        with self.assertRaises(ValueError) as ctx:
            lehmer_mean([], 2)
        self.assertEqual(str(ctx.exception), "lehmer_mean() needs at least one value [L1]")

    def test_cubic_mean_rule_d(self):
        self.assertAlmostEqual(cubic_mean([2, 2, 2]), 2)
        self.assertAlmostEqual(cubic_mean([1, 2, 3]), 2.2894284851066637)

    def test_cubic_mean_negative_rule_d(self):
        result = cubic_mean([-2, -2])
        self.assertIsInstance(result, float)
        self.assertAlmostEqual(result, -2)

    def test_cubic_mean_generator_rule_d(self):
        self.assertAlmostEqual(cubic_mean(v for v in [2, 2, 2]), 2)

    def test_cubic_mean_empty_rule_d(self):
        with self.assertRaises(ValueError) as ctx:
            cubic_mean([])
        self.assertEqual(str(ctx.exception), "cubic_mean() needs at least one value [L1]")

    def test_mean_of_squares_values_d5(self):
        self.assertAlmostEqual(mean_of_squares([1, 2, 3]), 14 / 3)

    def test_mean_of_squares_negative_d5(self):
        self.assertEqual(mean_of_squares([-2, 2]), 4)

    def test_mean_of_squares_generator_d5(self):
        self.assertEqual(mean_of_squares(v for v in [1, 2, 3]), mean_of_squares([1, 2, 3]))

    def test_mean_of_squares_empty_d5(self):
        with self.assertRaises(ValueError) as ctx:
            mean_of_squares([])
        self.assertEqual(str(ctx.exception), "mean_of_squares(): no values [L3]")

    def test_mean_of_squares_docstring_d5(self):
        self.assertTrue(mean_of_squares.__doc__.splitlines()[0].endswith(" [I4]"))

    def test_quartic_mean_values_d5(self):
        self.assertAlmostEqual(quartic_mean([2, 2, 2]), 2)
        self.assertAlmostEqual(quartic_mean([1, 2, 3]), (98 / 3) ** 0.25)

    def test_quartic_mean_negative_d5(self):
        self.assertAlmostEqual(quartic_mean([-2, -2]), 2)

    def test_quartic_mean_generator_d5(self):
        self.assertAlmostEqual(quartic_mean(v for v in [1, 2, 3]), quartic_mean([1, 2, 3]))

    def test_quartic_mean_empty_d5(self):
        with self.assertRaises(ValueError) as ctx:
            quartic_mean([])
        self.assertEqual(str(ctx.exception), "quartic_mean(): no values [L3]")

    def test_quartic_mean_docstring_d5(self):
        self.assertTrue(quartic_mean.__doc__.splitlines()[0].endswith(" [I4]"))

    def test_power_mean_values_d5(self):
        self.assertAlmostEqual(power_mean([1, 2, 3], 1), 2)
        self.assertAlmostEqual(power_mean([3, 4], 2), math.sqrt(12.5))
        self.assertAlmostEqual(power_mean([1, 4, 4], -1), 2.0)

    def test_power_mean_generator_d5(self):
        self.assertEqual(power_mean((v for v in [1, 2, 3]), 3), power_mean([1, 2, 3], 3))

    def test_power_mean_empty_d5(self):
        with self.assertRaises(ValueError) as ctx:
            power_mean([], 2)
        self.assertEqual(str(ctx.exception), "power_mean(): no values [L3]")

    def test_power_mean_zero_p_d5(self):
        with self.assertRaises(ValueError):
            power_mean([1, 2], 0)

    def test_power_mean_docstring_d5(self):
        self.assertTrue(power_mean.__doc__.splitlines()[0].endswith(" [I4]"))


if __name__ == "__main__":
    unittest.main()
