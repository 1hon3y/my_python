def qchet(num):
    if num % 2 == 0:
        return 'Чётное'
    else:
        return 'Нечётное'

x = input('Введите целое число: ')

if x:
    x = int(x)
    print(qchet(x))
else:
    print('Введите целое число!')
