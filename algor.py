import random
#Задаємо кількість кидків у мішень
n = int(input("Enter the count of shots at the target: "))
count = 0

#Задаємо функції для перевірки умов
def check_1():
    return x**2 + y**2 <= 1 and x<= 0 and y>= 0 and x <= - y
def check_2():
    return x**2 + y**2 <= 4 and x**2 + y**2 >= 1 and x >= 0 and y<=0 and x <= - y

def getPoint():
    x = random.uniform(-2,2)
    y = random.uniform(-2,2)
    return x, y

#Заходимо в цикл рандомних значень на заданому діапазоні мішені
for i in range(n):
    x, y = getPoint()
#Перевіримо виконання умов для знайдених значень
    if check_1() or check_2():
        count += 1
#Виводимо результат кількісь влучань, попавших в ціль
print("The point hit the target ",count," times")
#Обчислюмо площу заштрихованого діапазону
square = count/n*4*4
#Виводимо значення площі заштрихованого діапазону
print("Square = ",square," square units")
