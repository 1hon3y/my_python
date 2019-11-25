import math

def f(x):
    if 0.2<=x<=0.9:
        return math.sin(x)
    else:
        return 1

y=float(input('Введите число:'))
print('Значение функции:',f(y))
