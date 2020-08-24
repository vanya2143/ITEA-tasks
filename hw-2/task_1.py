# 1. Написать функцию, которая будет принимать на вход натуральное число n,
# и возращать сумму его цифр. Реализовать используя рекурсию
# (без циклов, без строк, без контейнерных типов данных).
# Пример: get_sum_of_components(123) -> 6 (1+2+3)

def get_sum_of_components_two(n):
    res = 0

    def my_func(num):
        nonlocal res
        num = int(num)
        if num != 0:
            res += (num % 10)
            return my_func(num / 10)

    my_func(n)
    return res


if __name__ == '__main__':
    print(get_sum_of_components_two(123))
