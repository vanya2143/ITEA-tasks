"""
1. Определить количество четных и нечетных чисел в заданном списке. 
Оформить в виде функции, где на вход будет подаваться список с целыми числами. 
Результат функции должен быть 2 числа, количество четных и нечетных соответственно.
"""


def list_check(some_list):
    even_numb = 0
    not_even_numb = 0

    for elem in some_list:
        if elem % 2 == 0:
            even_numb += 1
        else:
            not_even_numb += 1

    return f"even: {even_numb}, not even: {not_even_numb}"


if __name__ == '__main__':
    my_list = list(range(1, 20))
    print(list_check(my_list))
