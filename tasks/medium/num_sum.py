"""
Написать рекурсивную функцию sum_of_numbers, которая будет вычислять сумму
цифр целого числа.

Можно пользоваться только функциями, операторами и условиями.
"""


def sum_of_numbers(n: int):
    summa = 0
    while n > 0:
        digit = n % 10
        summa = summa + digit
        n = n // 10
    return summa


print(sum_of_numbers(123456))
