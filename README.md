# NexKit sandbox

A tiny project for trying the [NexKit](https://github.com/phuongnse/nexkit) pipeline.
Run the tests with `python3 -m unittest discover -s tests -v`.

## Functions

- `mean(values)` - the average of the values (any iterable). Raises `ValueError` if `values` is empty.
- `median(values)` - the middle value, or the average of the two middle values. Raises `ValueError` if `values` is empty.
- `mode(values)` - the most common value; on a tie, the smallest of them. Raises `ValueError` if `values` is empty.
- `spread(values)` - the largest value minus the smallest. Raises `ValueError` if `values` is empty.
- `variance(values)` - population variance: the mean of the squared differences from the mean. Raises `ValueError` if `values` is empty.
- `midrange(values)` - the average of the smallest and largest value. Raises `ValueError` if `values` is empty.
- `stdev(values)` - population standard deviation: the square root of the variance. Raises `ValueError` if `values` is empty.
- `sum_of_squares(values)` - the sum of each value squared. Raises `ValueError` if `values` is empty.
- `harmonic_mean(values)` - the number of values divided by the sum of their reciprocals. Raises `ValueError` if `values` is empty or any value is not positive.
- `geometric_mean(values)` - the n-th root of the product of the values. Raises `ValueError` if `values` is empty or any value is not positive.
- `trimmed_mean(values, k)` - the average after leaving out the `k` smallest and `k` largest values. Raises `ValueError` if `values` is empty, `k` is not a whole number 0 or more, or no values would be left.
- `count_above(values, threshold)` - how many values are strictly greater than `threshold` (any iterable). Returns 0 if `values` is empty.
- `percentile(values, q)` - the value at the `q`-th percent (0 to 100) by linear interpolation between the closest ranks, as numpy does. Raises `ValueError` if `values` is empty or `q` is outside 0 to 100.
- `describe(values)` - a dict with `count`, `mean`, `median`, `stdev` (population) and `p90` (the 90th percentile, from `percentile`). Raises `ValueError` if `values` is empty.
- `load_points(path)` - reads a CSV file of `x,y` lines (module `geometry`) and returns a list of `(x, y)` float tuples. Skips blank lines. Raises `ValueError` naming the line number if a line is not two numbers.
- `distance(p, q)` - the Euclidean distance between two points (module `geometry`).
