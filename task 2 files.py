#есть папка, в ней есть файлы с разными раcширениями.

#Нужно
#- по запросу пользователя показать все файлы с заданным расширением
#- по запросу пользователя показать файлы с совпадениями в имени (поиск)

import os
files = os.listdir("E:projects/studyPython/work_folder")
print ('Введите расширения файла')
extension = input()

for file in files:
    if file.endswith("." + extension):
        print(file)
