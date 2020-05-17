# 2. Используя модуль unittests написать тесты: сложения двух матриц, умножения матрицы и метод transpose

import unittest
from .task_1 import Matrix, MatrixSizeError


class TestMatrix(unittest.TestCase):
    def setUp(self) -> None:
        self.matrix_1 = Matrix([[1, 2, 9], [3, 4, 0], [5, 6, 4]])
        self.matrix_2 = Matrix([[2, 3, 0], [1, 2, 3], [5, 6, 4]])

        self.matrix_3 = Matrix([[2, 9], [4, 0], [6, 4]])
        self.matrix_4 = Matrix([[2, 9], [4, 0], [6, 4]])

    def test_add(self):
        self.assertEqual(self.matrix_1 + self.matrix_2, [[3, 5, 9], [4, 6, 3], [10, 12, 8]])
        self.assertEqual(self.matrix_3 + self.matrix_4, [[4, 18], [8, 0], [12, 8]])

        with self.assertRaises(MatrixSizeError):
            self.matrix_1 + self.matrix_3

    def test_mul(self):
        self.assertEqual(self.matrix_1 * 2, [[2, 4, 18], [6, 8, 0], [10, 12, 8]])
        self.assertEqual(self.matrix_1 * 2.5, [[2.5, 5.0, 22.5], [7.5, 10.0, 0.0], [12.5, 15.0, 10.0]])

    def test_transpose(self):
        self.assertEqual(self.matrix_1.transpose(), [[1, 3, 5], [2, 4, 6], [9, 0, 4]])
        self.assertEqual(self.matrix_1.transpose(), [[1, 2, 9], [3, 4, 0], [5, 6, 4]])


if __name__ == '__main__':
    unittest.main()
