"""
Написать генератор fibonacci, которая принимает номер значения num_count
из чисел Фибоначчи и выводит на экран результат до заданного значения.

Номер значения нужно проверить

Пример:

fibonacci(0) -> raise ValueError('Введите значение больше 1')
fibonacci(5)
1
2
3
5
8
Traceback (most recent call last):
File «C:/Python/Python3/python_generator.py», line 29, in
print(next(fib))
StopIteration
"""


num_count = input('Введите количество чисел\n')
num_count = int(num_count)


def fibonacci(n: int):
    a, b = 1, 1
    for i in range(n):
        yield a
        a, b = b, a + b
    if n == 0:
        print("raise ValueError('Введите значение больше 1')")


for j in fibonacci(num_count):
    print(j)



