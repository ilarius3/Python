import sys
number = int (input())
#9223372036854775807 = max_size най-голямото число според пайтън
max_number = -sys.maxsize #може да се направи и без сис, може да си напишем примерно -100000000000000
min_number = sys.maxsize	#но ние сме професионалисти, експерти и работим със сис
				#Библиотека се отваря като отиваме с мишката върху сис, натискаме Cntrl и щракваме 				отгоре с мишката
for num in range (number):
    current_number = int(input())
    if current_number > max_number:
        max_number = current_number
    if current_number < min_number:
        min_number = current_number
print (f'Max number: {max_number}')
print (f'Min number: {min_number}')
