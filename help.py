from pywebio.input import input 
from pywebio.output import put_text

name = input("и зачем ты тут? \nопять без меня пример не можешь решить? ")
put_text("так и думал! ладно неуч ")
choice = input('''
выбери что хочешь:
+ для добавления
- для вычитания
* для умножения
/ для разделения
''')

num_1 = int(input('ну давай пиши первое число неуч: '))
num_2 = int(input('жду теперь второе число неуч =D: '))

if choice == '+':
    put_text('{} + {} = '.format(num_1, num_2))
    put_text(num_1 + num_2)

elif choice == '-':
    put_text('{} - {} = '.format(num_1, num_2))
    put_text(num_1 - num_2)

elif choice == '*':
    put_text('{} * {} = '.format(num_1, num_2))
    put_text(num_1 * num_2)

elif choice == '/':
    put_text('{} / {} = '.format(num_1, num_2))
    put_text(num_1 / num_2)

else:
    put_text('Enter a valid operator, please run the program again.')

hel = input("ты серьзно не мог это решить? ")
put_text("ну ты даёшь...")
input("ладно, если что-то надо будет, я тут буду. ")
