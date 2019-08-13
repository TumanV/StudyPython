#Получить от пользователя двузначное число и вывести, какая цифра в нем большая, а какая меньшая.
#Например пользователь ввел 27. Результат: 2 - меньшая цифра, 7 - большая.
print ("Введите двузначное число")
number = int(input())
first_digit = number // 10
last_digit = number % 10

if first_digit > last_digit:
    max = first_digit
    min = last_digit
else:
    max = last_digit
    min = first_digit
print (max, "Большее число", min, "Меньшее число")



print('Введите двузначное число');

number = int(input())

first_digit = number // 10
last_digit = number % 10

print('Большее число:', max(first_digit, last_digit));
print('Меньшее число:', min(first_digit, last_digit));
