#Получить от пользователя строку текста и записать ее в файл
 #Спросить, желает ли пользователь ввести еще одну строку
 #Если нет, то сохранить файл
 #Если да, то записать еще одну строку

string = input ('Введите строку: ' + '\n')
file = open ('tuman.txt', 'a')
file.write (string)
file.write ('\n')
file.close()

print = input('Желаете ввести еще одну строку?')
second_string = str ('да')
if second_string:
    print = str('да')
second_string = input('Введите строку: ' + '\n')
second_file = open('tuman.txt', 'a')
second_file.write(second_string)
