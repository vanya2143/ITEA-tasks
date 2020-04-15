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
