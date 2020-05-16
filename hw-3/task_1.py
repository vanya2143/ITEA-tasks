# Реализовать некий класс Matrix, у которого:
# 1. Есть собственный конструктор, который принимает в качестве аргумента - список списков,
# копирует его (то есть при изменении списков, значения в экземпляре класса не должны меняться).
# Элементы списков гарантированно числа, и не пустые.

# 2. Метод size без аргументов, который возвращает кортеж вида (число строк, число столбцов).

# 3. Метод transpose, транспонирующий матрицу и возвращающую результат (данный метод модифицирует
# экземпляр класса Matrix)

# 4. На основе пункта 3 сделать метод класса create_transposed, который будет принимать на вход список списков,
# как и в пункте 1, но при этом создавать сразу транспонированную матрицу.
#
# https://ru.wikipedia.org/wiki/%D0%A2%D1%80%D0%B0%D0%BD%D1%81%D0%BF%D0%BE%D0%BD%D0%B8%D1%80%D0%


class Matrix:
    def __init__(self, some_list):
        self.data_list = some_list.copy()

    def size(self):
        row = len(self.data_list)
        col = len(self.data_list[0])
        return tuple([row, col])

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
    my_list = [[1, 2, 9], [3, 4, 0], [5, 6, 4]]

    t = Matrix(my_list)
    t.transpose()
    print(t.data_list)

    t2 = Matrix.create_transposed(my_list)
    print(t2.data_list)
