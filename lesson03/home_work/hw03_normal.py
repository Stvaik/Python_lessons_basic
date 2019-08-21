# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

def fibonacci(n, m):
    pass


for Y in range(0, 5 + 1):
    print(Y)

def fibonacci(n, m):
    a = []
    golden = 1.618034
    for i in range(n, m + 1):
        x = (golden ** i - (1 - golden) ** i) / (5 ** (1 / 2))
        a.append(round(x))
    return a

x = 5
y = 7

B = fibonacci(x, y)

print(B)
# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()


def sort_to_max(origin_list):
    n = 1
    while n < len (origin_list):
        for i in range(len(origin_list) - n):
            if origin_list[i] > origin_list[i + 1]:
                origin_list[i], origin_list[i + 1] = origin_list[i + 1], origin_list[i]
        n += 1
    return origin_list

print(sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0]))

# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.
def filter_function(func,iterable):
    output_iterable = []
    for i in range(len(iterable)):
        if func(iterable[i]) == True:
            output_iterable.append(iterable[i])
    return output_iterable

func = lambda x: type(x) == str
iterable = [-1, 2, 'a', 4, 'GGG']
print(filter_function(func,iterable))
# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.

