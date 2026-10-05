"""Small statistics helpers."""


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
