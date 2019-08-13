#Получить от пользователя число и вывести число разрядов
print("Введите число")
n = int(input())
n = abs(n)

count = 1
n //= 10

while n > 0:
    n //= 10
    count += 1

print(count)