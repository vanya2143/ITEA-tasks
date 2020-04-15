def search_item(some_list, find_item):
    some_list.sort()
    list_length = len(some_list)
    start = 0
    end = list_length - 1
    mid = list_length // 2
    i = 0

    while i < list_length:
        if find_item == some_list[mid]:
            return f'Число {some_list[mid]}, найдено по индексу {mid}'

        elif find_item > some_list[mid]:
            start = mid + 1
            mid = start + (end - start) // 2

        else:
            end = mid - 1
            mid = (end - start) // 2

        i += 1

    else:
        return f'Числа {find_item} нету в списке!'


if __name__ == '__main__':
    # my_list = list(range(0, 100))
    my_list = [1, 23, 33, 54, 42, 77, 234, 99, 2]
    my_item = 42

    print(search_item(my_list, my_item))
