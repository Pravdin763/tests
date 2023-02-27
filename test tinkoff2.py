# https://edu.tinkoff.ru/selection/76378fbd-1998-48fa-944e-eb736d321f11/exam/244?task=5

n, k = int(input()), int(input())
nums = []
i = n
wt = int('1'*(len(str(i))))
while i<=k:
    if len(set(str(i)))==1:
        nums.append(i)
        i +=wt
    else:
        i+=1
print(len(nums))


