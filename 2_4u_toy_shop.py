excursion_prise = float(input())
puzzles_num = int(input())
dolls_num = int(input())
bears_num = int(input())
minions_num = int(input())
trucks_num = int(input())
puzzles = puzzles_num * 2.60
dolls = dolls_num * 3
bears = bears_num * 4.10
minions = minions_num * 8.2
trucks = trucks_num * 2
num_sells = puzzles_num + dolls_num + bears_num + minions_num + trucks_num
all_sells = puzzles + dolls + bears + minions + trucks
if num_sells >= 50:
    all_sells *= 0.75 # или all_sells -= 0.25
profit = all_sells*0.9 #    all_sells -= all_sells*0.1
left_money = profit - excursion_prise
if left_money >= 0:
    print(f'Yes! {left_money:.2f} lv left.')
else:
    print(f'Not enough money! {-1*left_money:.2f} lv needed.')
