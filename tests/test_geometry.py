import os
import tempfile
import unittest

from geometry import distance, load_points


class GeometryTests(unittest.TestCase):
    def _load(self, text):
        with tempfile.TemporaryDirectory() as d:
            path = os.path.join(d, "points.csv")
            with open(path, "w") as f:
                f.write(text)
            return load_points(path)

    def test_distance(self):
        self.assertEqual(distance((0, 0), (3, 4)), 5.0)

    def test_load_points_skips_blank_line(self):
        self.assertEqual(self._load("1,2\n\n3.5,4\n-1,0\n"), [(1.0, 2.0), (3.5, 4.0), (-1.0, 0.0)])

    def test_load_points_bad_line(self):
        for text in ["1,2\n3\n", "1,2\na,b\n", "1,2\n1,2,3\n"]:
            with self.assertRaises(ValueError) as ctx:
                self._load(text)
            self.assertIn("line 2", str(ctx.exception))

    def test_load_points_empty_file(self):
        self.assertEqual(self._load(""), [])


if __name__ == "__main__":
    unittest.main()
