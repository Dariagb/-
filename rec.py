


def f(a,b):
    if b==0:
        return 1
    elif b==1:
        return a
    elif b<0:
        return 1/f(a,-b)
    else:
        return a*f(a,b-1)

print(f(a,b))    
a=int(input("введите первое число"))
b=int(input("введите второе число"))


def sum(a, b):
    if a==0:
        return b
    else:
        return sum(a -1, b +1)
a=int(input("введите первое число"))
b=int(input("введите второе число"))
print(sum(a,b))