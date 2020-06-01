import unittest

from angem.matrix import Matrix


class MatrixTestCase(unittest.TestCase):
    def test_matrix_is_always_rectangular(self):
        self.assertRaises(
            AssertionError,
            lambda: Matrix(
                (1, 2, 3),
                (1, 2),
                (1, 2, 3),
            )
        )

    def test_matrix_size(self):
        self.assertEqual(
            Matrix(
                (1, 2, 3),
                (1, 2, 8),
            ).size().strings,
            ((3, 2), )
        )

    def test_matrix_zero(self):
        self.assertEqual(
            Matrix.zero(3, 4).strings,
            (
                (0, 0, 0),
                (0, 0, 0),
                (0, 0, 0),
                (0, 0, 0),
            )
        )

    def test_matrix_getitem(self):
        self.assertEqual(
            Matrix(
                (1, 2, 3),
                (1, 2, 8),
            )[1, 2],
            8
        )


if __name__ == '__main__':
    unittest.main()
