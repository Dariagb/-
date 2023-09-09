"""name = input("введите имя")
family = input("введите фамилию ")
print(f"Здравствуйте,{name} {family}")"""
import math

"""print("Как дела? \nОтлично!")

number1 = (int(input("введите первое число:")))
number2 = (int(input("введите второе число:")))
number3 = (int(input("введите третье число:")))
print(f"Результат: {(number1 + number2)*number3}")

fraction = int(input("Сколько количество кусков было?"))
fraction1 = int(input("Сколько съели:"))
print(f"осталось:{fraction-fraction1}")"""

"""name = input("Введите ваше имя:")
age = int(input("введите возраст:"))
print(f"{name},через год вам будет {age+1}")"""

"""total_account =(int(input("введите общий счет:")))
number_of_participants = (int(input("Количество участников: ")))
res = total_account/ number_of_participants
print(res)"""

"""day = int(input("введите промежуток:"))
print(f'{day*24}- количество часов, {day*1440}-количество минут, {day*86400}-количество секунд')"""

"""f = int(input("введите кг:"))
res = f * 2.204
print(res)"""

"""k = int(input("введите число больше 100"))
l = int(input("введите число меньше 10"))
e = int(k/l)
print(e)"""

#12
"""numbers = int(input("введите первое число:"))
n = int(input("введите второе число:"))
if numbers > n:
    print(n)
else:
    print(numbers, n)"""

#13
"""numbers = int(input("введите первое число меньше 20:"))
if numbers>= 20:
    print("Too high")
else:
    print("Thank you")"""

#14
"""numbers = int(input("введите первое число от 10 до 20:"))
if numbers>=10 and numbers<=20:
    print("thank you")
else:
    print("Incorrect answer")"""
#15
"""numbers = str(input("введите любимый цвет"))
if numbers == "red" or numbers == "Red":
    print("ok")"""
#16
"""n = str.lower(input("Идет ли дождь?"))
if n == "да":
    d = str.lower(input("Ветрено?"))
    if d == "да":
        print("Возьми зонт")
    else:
        print("Отлично")
else:
    print("Сегодня хорошая погода")"""

#17
"""n = int(input("введите возраст:"))
if n>=18:
    print("Смотри")
elif n==17:
    print("мал")
else:
    print("карапуз" )"""

#18
"""n = int(input("введите число:"))
if n < 10:
    print("Too low")
elif n >=10 and n<=20:
    print("Correct")
else:
    print("Too high")"""

#20
"""numbers = input("введите имя:")
print(len(numbers))"""

#21
"""name = input("введите имя")
family = input("введите фамилию ")
h = name+family
print(len(h))"""

#22
"""name = input("введите имя")
family = input("введите фамилию ")
print(name.title()+family.title())"""

#23
"""name = input("введите строку")
print(len(name))
n = name[0:-1]
print(n)"""

#24

"""name = input("введите имя")
print(name.upper())"""

#25
"""name = input("введите имя")
if len(name) < 5:
    femeli = input("Введите фамилию")
    print(name.upper()+femeli.upper())
else:
    print(name.lower())"""

#27
"""name = float(input("введите число "))
res = name*2
print(round(res,1))"""

#28
#29
"""name = int(input("введите число больше 500 "))
res= math.sqrt(name)
print(round(res,2))"""
#30
"""p = math.pi
print(round(p,5))"""
#31
"""name = int(input("введите радиус круга:"))
p = math.pi
print(name **2*p)"""

#32
"""name = int(input("введите радиус:"))
p = int(input("введите высоту:"))
e = math.pi
res = name **2*e
y=res*p
print(round(y,3))"""

#33
"""name = int(input("введите число:"))
name1 = int(input("введите число:"))
res =name//name1
res2 =name %name1
print(res, res2)"""

#34
"""name = int(input("введите 1  или 2:"))
if name == 1:
    len= int(input(" введите длину стороны квадрата:"))
    print(len**2)
elif name == 2:
    len2 =int(input(" введите длину стороны треугольника:"))
    len3 =int(input(" введите высоту треугольника:"))
    print(0.5*len2*len3)
else:
    print("ошибка")"""

#35
"""name = input("введите имя")
for i in range(3):
    print(name)"""
#36
"""name = input("введите имя")
numbers = int(input("введите число"))
for i in range(numbers):
    print(name)"""
#37
"""name = input("введите имя")
for i in name:
    print(i)"""

#38
"""name = input("введите имя")
numbers = int(input("введите число"))
for i in name:
    for y in range(numbers):
        print(i)"""
#39
"""numbers = int(input("введите число"))
for i in range(1,13):
    res =i*numbers
print(i, "x", numbers, "=", res)"""

#40
"""numbers = int(input("введите число до 50"))
if numbers > 50:
            print("задано не верно")
else:
     for i in range(50,numbers-1,-1):
         print(i)"""
#41
"""numbers = int(input("введите число до 50"))
name = input("введите имя")
if numbers<10:
    for i in range(numbers):
        i+=1
        print(name)
else:
    for j in range (3):
        print("dfghj")"""
#42

"""total = 0
for i in range (0,5):
    а = int(input("Введите число"))
    n = input("хотите это число внести в сумму?")
    if n=="да":
       total = a+total
print(total)"""

#43
"""n =input("какой порядок выбрать:")
if n == "прямой":
    numbers= int(input("введите число:"))
    for i in range(1,numbers+1):
        print(i)
elif n =="обратный":
    numbers1 = int(input("введите число меньше 20:"))
    for j in range(20,numbers1+1,-1):
        print(j)
else:
    print("dfg")"""

#44
numbers = int(input("сколько людей пригласить на вечеринку?"))
if numbers <=10:
    n=input("введите имя:")
    for i in range(0, numbers):
        print(f"{n} привет")
if numbers > 10:
    print("kjhgfd")













