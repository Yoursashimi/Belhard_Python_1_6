"""
Написать функцию count_char, которая принимает строковое значение STR_VAL,
из которого создает и возвращает словарь, следующего вида:
{
    'буква': количество-вхождений-в-строку
}

например: {
    'p': 2,
    'y': 1,
    ...
}

Нельзя пользоваться collections.Counter!
"""
STR_VAL = 'python is the fastest-growing major programming language'


def count_char(some_string: str):
    count = {}
    for i in some_string:
        if i not in count:
            count[i] = 1
        else:
            count[i] += 1
    return count


print(count_char(STR_VAL))
