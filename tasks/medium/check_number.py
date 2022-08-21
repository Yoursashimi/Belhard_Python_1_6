"""
Написать рекурсивную функцию check_number, которая должна возвращать True,
если переданное ей число n является степенью двойки (1 тоже степень двойки) и
False, если нет

Нельзя пользоваться операцией возведения в степень
"""


from math import log


def check_number(number) -> bool:
    logn = log(number, 2)
    if logn == int(logn):
        return True
    else:
        return False


print(check_number(3))
