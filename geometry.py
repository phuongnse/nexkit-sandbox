"""Points: load them from a CSV file and measure the distance between two."""
import math


def distance(p, q):
    """Return the Euclidean distance between points p and q."""
    return math.hypot(p[0] - q[0], p[1] - q[1])


def load_points(path):
    """Read a CSV of x,y lines and return a list of (x, y) float tuples."""
    points = []
    with open(path, newline='') as f:
        for n, line in enumerate(f, 1):
            line = line.strip()
            if not line:
                continue
            parts = line.split(',')
            if len(parts) != 2:
                raise ValueError(f'load_points() bad line {n}')
            try:
                points.append((float(parts[0]), float(parts[1])))
            except ValueError:
                raise ValueError(f'load_points() bad line {n}') from None
    return points
