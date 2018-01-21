"""def intersect(*args):
    res = [ ]
    for x in args[0]:                      # Сканировать первую последовательность
        for other in args[1:]:              # Во всех остальных аргументах
            if x not in other: break          # Общий элемент?
        else:                                     # Нет: прервать цикл
            res.append(x)                       # Да: добавить элемент в конец
    return res





def union(*args):
    res = [ ]
    for seq in args:                      # Для всех аргументов
        for x in seq:                          # Для всех элементов
            if not x in res:
                res.append(x)                       # Добавить новый элемент в результат
    return res
"""
"""
def mysum(L):
    print(L)
    if not L:
        return 0
    else:
        return L[0] + mysum(L[1:]) # Вызывает себя саму
F = [1, 2, 3, 4, 5]
G=mysum(F)
print(G)
"""
def mysum(L):
    return 0 if not L else L[0] + mysum(L[1:])          # Трехместный оператор


def mysum(L):                                                                     # Суммирует любые типы
    return L[0] if len(L) == 1 else L[0] + mysum(L[1:])               # предполагает наличие
                                                                                            # хотя бы одного значения

def mysum(L):                                                                          # Использует расширенную
    first, *rest = L                                                                        # операцию присваивания
    return first if not rest else first + mysum(rest)                       # последовательностей


def mysum(L):
    if not L: return 0
    return nonempty(L)                                    # Вызов функции, которая вызовет эту функцию
def nonempty(L):
    return L[0] + mysum(L[1:])                         # Косвенная рекурсия

























# в Python 3.0
