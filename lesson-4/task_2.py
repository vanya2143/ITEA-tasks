# К реализованному классу Matrix в Домашнем задании 3 добавить следующее:
# 1. __add__ принимающий второй экземпляр класса Matrix и возвращающий сумму матриц,
# если передалась на вход матрица другого размера - поднимать исключение MatrixSizeError
# (по желанию реализовать так, чтобы текст ошибки содержал размерность 1 и 2 матриц - пример:
# "Matrixes have different sizes - Matrix(x1, y1) and Matrix(x2, y2)")

# 2. __mul__ принимающий число типа int или float и возвращающий матрицу, умноженную на скаляр

# 3. __str__ переводящий матрицу в строку.
# Столбцы разделены между собой табуляцией, а строки — переносами строк (символ новой строки).
# При этом после каждой строки не должно быть символа табуляции и в конце не должно быть переноса строки.
#


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
    list_1 = [[1, 2, 9], [3, 4, 0], [5, 6, 4]]
    list_2 = [[2, 3, 0], [1, 2, 3], [5, 6, 4]]
    list_3 = [[2, 3], [1, 2], [5, 6]]

    t1 = Matrix(list_1)
    t1.transpose()

    t2 = Matrix.create_transposed(list_2)

    t3 = Matrix(list_3)

    print("t1: ", t1.data_list)
    print("t2: ", t2.data_list)
    print("t3: ", t3.data_list)

# __add__
    print("\n__add__ t1 + t2: ", t1 + t2)

    try:
        print("\nПробую: t1 + t3")
        print(t1 + t3)
    except MatrixSizeError:
        print('Тут было вызвано исключение MatrixSizeError')

# __mul__
    print("\n__mul__ t2 * 3: \n", t2 * 3)

# __str__
    print('\n__str__ t1')
    print(t1)
