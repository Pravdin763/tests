# https://edu.tinkoff.ru/selection/76378fbd-1998-48fa-944e-eb736d321f11/exam/244?task=12
# https://www.cyberforum.ru/python-tasks/thread2775648.html
# Артемия есть бесконечное число монет, каждая из которых одного из трех номиналов. Его интересует, какие суммы от
# 1 до n рублей он может набрать в свой кошелек, если там заранее лежала монета величиной в


n = int(input())

a1, a2, a3 = map(int, input().split())

result = sum(a1 * i + a2 * j + a3 * k <= n for i in range(n) for j in range(n - a1 * i) for k in range(n - a1 * i - a2 * j))
print(result)