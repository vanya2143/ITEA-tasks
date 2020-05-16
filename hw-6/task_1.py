# 1. Реализовать подсчёт елементов в классе Matrix с помощью collections.Counter.
# Можно реализовать протоколом итератора и тогда будет такой вызов - Counter(maxtrix).
# Либо сделать какой-то метод get_counter(), который будет возвращать объект Counter и подсчитывать все элементы
# внутри матрицы. Какой метод - ваш выбор.
#
# 2. Используя модуль unittests написать тесты: сложения двух матриц, умножения матрицы и метод transpose


class MatrixSizeError(Exception):
    pass


class Matrix:
    def __init__(self, some_list):
        self.data_list = some_list.copy()

    def __add__(self, other):
        row, col = self.size()

        if self.size() != other.size():
            raise MatrixSizeError(
                f'Matrixes have different sizes - Matrix{self.size()} and Matrix{other.size()}'
            )

        return [
            [self.data_list[j][i] + other.data_list[j][i] for i in range(row)] for j in range(col)
        ]

    def __mul__(self, other):
        return [[item * other for item in row] for row in self.data_list]

    def __str__(self):
        return ''.join('%s\n' % '\t'.join(map(str, x)) for x in self.data_list).rstrip('\n')

    def size(self):
        row = len(self.data_list)
        col = len(self.data_list[0])
        return row, col

    def transpose(self):
        _, col = self.size()
        t_matrix = [
            [item[i] for item in self.data_list] for i in range(col)
        ]
        self.data_list = t_matrix
        return self.data_list

    @classmethod
    def create_transposed(cls, int_list):
        obj = cls(int_list)
        obj.transpose()
        return obj


if __name__ == '__main__':
    pass
