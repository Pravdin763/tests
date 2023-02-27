# https://edu.tinkoff.ru/selection/76378fbd-1998-48fa-944e-eb736d321f11/exam/244?task=6
# https://github.com/PeaceAndLove1337/SomeTasksOnKotlin/blob/master/src/main/kotlin/ThirdExample.kt
n = int(input())
nums = [int(input()) for i in range(n)]
even = -1
uneven = -1
count = 0
for i, k in enumerate(nums):
    if k % 2 == 0:
        count += 1
    if (i + 1) % 2 != 0:
        if k % 2 == 0:
            uneven = i + 1
    else:
        if k % 2 != 0:
            even = i + 1
if even == -1 or uneven == -1 or len(nums) // 2 != count:
    print(-1, -1)
else:
    print(uneven, even)
