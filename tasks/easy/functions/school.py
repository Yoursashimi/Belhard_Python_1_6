"""
Написать композицию из функций (не чистых функций)

Имеется словарь SCHOOL_DATA с данными школы класс-количество учеников

- Функция incr_students, которая принимает SCHOOL_DATA, название класса и
    увеличивает количество учеников на 1
- Функция decr_students, которая принимает SCHOOL_DATA, название класса и
    уменьшает количество учеников на 1, но не меньше 0
- Функция add_class, которая принимает SCHOOL_DATA, название класса и добавляет
    класс в словарь с количеством учеников 0
- Функция remove_class, которая принимает SCHOOL_DATA, название класса и удаляет
    класс из словаря
- Функция calc_students, которая принимает SCHOOL_DATA и возвращает кол-во
    учеников во всей школе
"""
school_data = {
    '1a': 15,
    '1b': 23,
    '2a': 13,
    '2b': 30
}


def incr_students(SCHOOL_DATA: dict, clas):
    SCHOOL_DATA[clas] = SCHOOL_DATA.get(clas, 0) + 1
    return SCHOOL_DATA


def decr_students(SCHOOL_DATA: dict, clas):
    SCHOOL_DATA[clas] = SCHOOL_DATA.get(clas, 0) - 1
    if SCHOOL_DATA[clas] == 0:
        return SCHOOL_DATA
    return SCHOOL_DATA


def add_class(SCHOOL_DATA: dict, new_klass):
    SCHOOL_DATA[new_klass] = 0
    return SCHOOL_DATA


def remove_class(SCHOOL_DATA, clas: dict):
    SCHOOL_DATA.pop(clas)
    return SCHOOL_DATA


def calc_students(SCHOOL_DATA: dict):
    summa = 0
    for i in SCHOOL_DATA.values():
        summa += i
    return summa
