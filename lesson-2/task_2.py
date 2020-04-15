def all_numbers_sum(num1, num2):
    return sum([num for num in range(num1, num2 + 1)])


if __name__ == '__main__':
    print(all_numbers_sum(1, 5))
