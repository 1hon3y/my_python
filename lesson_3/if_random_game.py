import random

x=random.randint(1,4)
if x:
    y=int(input('Введите число:'))
    if y==x:
        print('Победа!')
    else:
        if y<x:
            print('Меньше загаданного!')
        else:
            print('Больше загаданного!')
        print('Попробуйте ещё раз!')
        
else:
    print('Число не введено!!')
