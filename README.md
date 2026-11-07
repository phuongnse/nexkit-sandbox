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
