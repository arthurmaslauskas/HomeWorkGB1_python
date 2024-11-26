# 1 урок - Ввод - вывод, операторы ветвления
# 1 ЗАДАЧА Способ целочисленное деление растояние N-проехали
# m - растояние которое должен проехать
# после нужно, чтобы получилось 2 дня пути
# вот решение связано на алгоритме с добавлением логики

# n = int(input("Write n: "))
# m = int(input("Write m: "))

# print((m+(n-1)) // n)

# Делам просто на коде
# print((-m) // n) * (-1)

#2 ЗАДАЧА 
# есть 3 класса и есть 3 числа это 20 21 22 это дети 
# и нужно носчитать кол-во парт и должно быть 32
# МОё
# def child():
#     child_user = input("Write Child: ")
#     user_split = [int(num) for num in child_user.split()]
    
#     split_max = sum(user_split) // 2 + 1
#     return split_max
    
# result = child()
# print(result)

#этот вариант лучше, так как мы сделали с помощью функции
#а решение учителя примитивнее (на мой взгляд)

# a = int(input("A: "))
# b = int(input("B: "))
# c = int(input("C: "))
# desks = (a + 1) // 2 +( b + 1) // 2 + (c + 1) // 2
# print(f"Total: {desks}")

# 3 Задача( Нужно сделать задачу,
# которую он пытается понять высокостный год или нет)

# (Это мое решение и я считаю его самым информативным)

# def four_years(num):
#     if num % 4 == 0:
#         return True
#     else:
#         return False
    
# years = int(input("Write your years: "))

# result = four_years(years)
# print(result)

# (Решение преподавателя)
# a = int(input("Write years: "))
# if (a%4 ==0 and a%100 !=0) or (a%400 !=0):
#     print("Yes")
# else:
#     print("No")