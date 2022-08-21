"""
Написать генератор get_even_number, который возвращает подряд четные числа

Например:

even_gen = get_even_number()

next(even_gen) -> 2
next(even_gen) -> 4
next(even_gen) -> 6
"""


def get_even_number():
    for i in range(1, 100):
        if i % 2 == 0:
            yield i


even_gen = get_even_number()


next(even_gen)

