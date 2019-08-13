#Получить от пользователя число и вывести, простое оно или нет
#Простыми являются натуральные числа больше 1, которые делятся нацело только на 1 и самих себя

print('Введите число:')

number = int(input())
isSimple = True

for i in range(2, number, 1):
  if number % i == 0:
    isSimple = False
    break

if isSimple:
  print('Простое число')
else:
  print('Не простое число')
