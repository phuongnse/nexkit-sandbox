"""Small statistics helpers."""

import math
from collections import Counter


def mean(values):
    total = 0
    count = 0
    for v in values:
        total += v
        count += 1
    if count == 0:
        raise ValueError("mean() arg is an empty sequence")
    return total / count


def median(values):
    if not values:
        raise ValueError("median() arg is an empty sequence")
    ordered = sorted(values)
    mid = len(ordered) // 2
    if len(ordered) % 2:
        return ordered[mid]
    return (ordered[mid - 1] + ordered[mid]) / 2


def mode(values):
    """Return the most common value; on a tie, return the smallest of them."""
    if not values:
        raise ValueError("mode() arg is an empty sequence")
    counts = Counter(values)
    best = max(counts.values())
    return min(v for v, c in counts.items() if c == best)


def spread(values):
    """Return the largest value minus the smallest."""
    if not values:
        raise ValueError("spread() arg is an empty sequence")
    return max(values) - min(values)


def variance(values):
    """Return the population variance: the mean of squared differences from the mean."""
    if not values:
        raise ValueError("variance() arg is an empty sequence")
    m = mean(values)
    return sum((v - m) ** 2 for v in values) / len(values)


def midrange(values):
    """Return the mean of the smallest and largest value."""
    if not values:
        raise ValueError("midrange() arg is an empty sequence")
    return (min(values) + max(values)) / 2


def stdev(values):
    """Return the population standard deviation: the square root of the variance."""
    if not values:
        raise ValueError("stdev() arg is an empty sequence")
    return math.sqrt(variance(values))


def sum_of_squares(values):
    """Return the sum of each value squared."""
    if not values:
        raise ValueError("sum_of_squares() arg is an empty sequence")
    return sum(v ** 2 for v in values)


def harmonic_mean(values):
    """Return the number of values divided by the sum of their reciprocals."""
    if not values:
        raise ValueError("harmonic_mean() arg is an empty sequence")
    if any(v <= 0 for v in values):
        raise ValueError("harmonic_mean() requires positive values")
    return len(values) / sum(1 / v for v in values)


def geometric_mean(values):
    """Return the n-th root of the product of the values; all must be positive."""
    if not values:
        raise ValueError("geometric_mean() arg is an empty sequence")
    if any(v <= 0 for v in values):
        raise ValueError("geometric_mean() requires positive values")
    return math.exp(sum(math.log(v) for v in values) / len(values))
