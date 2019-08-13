#Получить от пользователя два числа и показать то, которое больше
print('Введите первое число:')
number1=input()
print
print('Введите второе число:')
number2=input()
print
if (number1 == number2):
    print('Значения равны')
elif (number1, "<" ,number2):
    print(number1, "<" ,number2)
else:
    print(number1, ">" ,number2)