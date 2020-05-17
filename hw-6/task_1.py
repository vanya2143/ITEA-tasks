# 1. Реализовать подсчёт елементов в классе Matrix с помощью collections.Counter.
# Можно реализовать протоколом итератора и тогда будет такой вызов - Counter(maxtrix).
# Либо сделать какой-то метод get_counter(), который будет возвращать объект Counter и подсчитывать все элементы
# внутри матрицы. Какой метод - ваш выбор.

from collections import Counter


class MatrixSizeError(Exception):
    pass


class Matrix:
    def __init__(self, some_list):
        self.data_list = some_list.copy()
        self.counter = Counter

    def __add__(self, other):
        if self.size() != other.size():
            raise MatrixSizeError(
                f'Matrixes have different sizes - Matrix{self.size()} and Matrix{other.size()}'
            )

        return [
            [self.data_list[row][col] + other.data_list[row][col] for col in range(self.size()[1])]
            for row in range(self.size()[0])
        ]

    def __mul__(self, other):
        return [[item * other for item in row] for row in self.data_list]

    def __str__(self):
        return ''.join('%s\n' % '\t'.join(map(str, x)) for x in self.data_list).rstrip('\n')

    def get_counter(self):
        return self.counter(elem for list_elem in self.data_list for elem in list_elem)

    def size(self):
        row = len(self.data_list)
        col = len(self.data_list[0])
        return row, col

    def transpose(self):
        t_matrix = [
            [item[i] for item in self.data_list] for i in range(self.size()[1])
        ]
        self.data_list = t_matrix
        return self.data_list

    @classmethod
    def create_transposed(cls, int_list):
        obj = cls(int_list)
        obj.transpose()
        return obj


if __name__ == '__main__':
    list_1 = [[1, 2, 9], [3, 4, 0], [5, 6, 4]]
    list_2 = [[2, 3], [1, 2], [5, 6]]

    matrix1 = Matrix(list_1)
    matrix2 = Matrix(list_2)

    print(matrix1.get_counter())
    print(matrix2.get_counter())
