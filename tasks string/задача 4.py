# Проверить, является ли строка палиндромом, например лазер боре хер обрезал
somestring  = str(input()).replace (' ', '')
a = somestring [::-1]
if somestring  == a:
  print("yes")
else:
  print("no")