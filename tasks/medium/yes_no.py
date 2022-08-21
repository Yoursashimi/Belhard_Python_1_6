"""
Напишите функцию yes_or_no, которая принимает список из целых чисел,
проходит по нему и выводит Yes, если число уже встречалось и No, если нет
"""


def yes_or_no(some_list: list):
    new_list = set()
    for i in some_list:
        if i in new_list:
            print('Yes')
        else:
            print('No')
            new_list.add(i)


print(yes_or_no([1, 2, 3, 4, 4, 3, 2]))
