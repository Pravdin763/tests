'''Вычислить максимальный медианный бал учеников (медианный, средний)
Первая строка содержит числа n и s (колличество учеников и Ограничение по баллам)
Гарантируется что n учеников - нечетное. Следующие n строк содержат числа j и r (минимальный и максимальный бал для ученика)
Найти максимальный медианный балл, при этом не выйти за пределы ограничения s'''

#n, s= map(int, input().split())                                            # с любыми числами
#spis = [[j for j in range(int(input(), int(input())+1))] for i in n]       # с любыми числами

#x = sorted([[11, 12, 13, 14], [2, 3, 4, 5, 6, 7, 8, 9, 10], [11, 12, 13, 14]])                 # пример 1 max_num = 27
x = sorted([[5, 5], [3, 4, 5], [7, 8, 9], [6, 7], [3, 4, 5, 6, 7, 8], [10, 10], [1, 1]])        # пример 2 max_num = 42
max_num = 42            #  МЕНЯТЬ ЧИСЛО 42 и 27 для тестов! или s
x = sorted(x, key = lambda z: max(z))                               # сортируем 2 раза, тут по максимальному числу

left = x[:len(x)//2]        # левая граница
right = x[len(x)//2:]       # правая граница, включая медианну

res = [None for i in range(len(x))]     # список результатов

for i, k in enumerate(left):            # для левой границы все просто, указываем самые плохие цоенки, чтобы больше осталось из s
    res[i] = min(k)

delta = max_num - sum(res[:len(x)//2])       # 33       # вычисляем разницу между s (ограничением) и левой границой, ДО медианного числа
t = sum(max(i) for i in right)   # 34       # сумма правой границы

while t > delta:
    for i, k in enumerate(right[::-1]):
        if len(k)!=2 and k[0]!=k[1]:        # не учитываем если длина списка=2 и числа одинаковые, например [10, 10]
            t -= k[-1]-k[-2]                # сокращаем t на разницу между последним(удаляемым) и предпоследним числом
            right[right.index(k)] = k[:-1]  # находим индекс списка и меняем его в right, сложность из за [::-1]
        if t <= delta:
            break

for i, k in enumerate(right, len(x)//2):
    res[i] = max(k)

print(res, 'сумма в диапазоне: ', sum(res), 'ответ = ',res[len(x)//2])
