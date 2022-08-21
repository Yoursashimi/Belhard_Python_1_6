"""
Написать генератор fibonacci, который возвращает подряд значения числе Фибоначчи

Например:

fibonacci_gen = fibonacci()

next(fibonacci_gen) -> 1
next(fibonacci_gen) -> 1
next(fibonacci_gen) -> 2
next(fibonacci_gen) -> 3
next(fibonacci_gen) -> 5
next(fibonacci_gen) -> 8
"""


def fibonacci():
    a, b = 1, 1
    for i in range(100):
        yield a
        a, b = b, a + b


fibonacci_gen = fibonacci()


print(next(fibonacci_gen))
print(next(fibonacci_gen))
print(next(fibonacci_gen))
print(next(fibonacci_gen))
print(next(fibonacci_gen))
