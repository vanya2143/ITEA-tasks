# 2. Написать декоратор log, который будет выводить на экран все аргументы,
# которые передаются вызываемой функции.
# @log
# def my_sum(*args):
# return sum(*args)
#
# my_sum(1,2,3,1) - выведет "Функция была вызвана с - 1, 2, 3, 1"
# my_sum(22, 1) - выведет "Функция была вызвана с - 22, 1"


def log(func):
    def wrapper(*args):
        res = func(*args)
        print("Функция была вызвана с - " + ', '.join(map(str, args)))
        return res

    return wrapper


@log
def my_sum(*args):
    return


if __name__ == '__main__':
    my_sum(11, 2, 3, 's', 4)
