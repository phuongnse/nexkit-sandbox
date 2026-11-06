"""Small statistics helpers."""

from collections import Counter


def mean(values):
    if not values:
        raise ValueError("mean() arg is an empty sequence")
    return sum(values) / len(values)


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
