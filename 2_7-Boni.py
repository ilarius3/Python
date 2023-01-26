num = float(input())
bonus = 0
if num <= 100:
    if num % 2 == 0:
        bonus = 6
    elif num % 10 == 5:
        bonus = 7
    else:
        bonus = 5
elif num <=1000:
    if num % 2 == 0:
        bonus = num*0.2 + 1
    elif num % 10 == 5:
        bonus = num*0.2 + 2
    else:
        bonus = num*0.2
elif num > 1000:
    if num % 2 == 0:
        bonus = num * 0.1 + 1
    elif num % 10 == 5:
        bonus = num * 0.1 + 2
    else:
         bonus = num * 0.1
print(bonus)
print(num+bonus)
