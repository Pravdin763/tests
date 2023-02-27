
# https://edu.tinkoff.ru/selection/76378fbd-1998-48fa-944e-eb736d321f11/exam/244?task=4
# https://itfy.org/threads/zadacha-na-ogranichenie-chisla-operacij.3087/
# https://ru.stackoverflow.com/questions/1422946/%d0%9d%d0%b0%d0%b9%d1%82%d0%b8-%d0%bc%d0%b0%d0%ba%d1%81%d0%b8%d0%bc%d0%b0%d0%bb%d1%8c%d0%bd%d1%83%d1%8e-%d1%80%d0%b0%d0%b7%d0%bd%d0%be%d1%81%d1%82%d1%8c-%d0%bc%d0%b5%d0%b6%d0%b4%d1%83-%d0%ba%d0%be%d0%bd%d0%b5%d1%87%d0%bd%d0%be%d0%b9-%d0%b8-%d0%bd%d0%b0%d1%87%d0%b0%d0%bb%d1%8c%d0%bd%d0%be%d0%b9-%d1%81%d1%83%d0%bc%d0%bc%d0%be%d0%b9/1423058#1423058

#У Кости есть бумажка, на которой написано n чисел. Также у него есть возможность не больше, чем k раз,
# взять любое число с бумажки, после чего закрасить одну из старых цифр, а на ее месте написать новую произвольную цифру.
#На какое максимальное значение Костя сможет увеличить сумму всех чисел на листочке?


n, k = int(input()), int(input())
nums = [int(input()) for i in range(n)]
delta = []

for i in nums:
    wt =1       # множитель
    while i>0:
        x = i%10
        delta.append((9-x)*wt)  # остаток от деления * множитель
        i = i//10
        wt*=10      # умножаем на 10 каждый раз, если число больше 9, 99 итд
print(sum(sorted(delta, reverse=True)[:k]))
