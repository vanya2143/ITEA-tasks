"""
1. Написать функцию, которая будет принимать на вход натуральное число n,
и возращать сумму его цифр. Реализовать используя рекурсию
(без циклов, без строк, без контейнерных типов данных).
Пример: get_sum_of_components(123) -> 6 (1+2+3)
"""


def get_sum_of_components_two(n):
    return 0 if not n else n % 10 + get_sum_of_components_two(n // 10)


if __name__ == '__main__':
    print(get_sum_of_components_two(123))
