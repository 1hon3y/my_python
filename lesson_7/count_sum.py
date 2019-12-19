a = input('Введите число: ')
sumkvad = 0

if a.isdigit():
    for i in list(a):
        if int(i) % 2 == 1:
            sumkvad += int(i)*int(i)
    print(f'Сумма квадратов нечетных цифр в числе:{sumkvad}')
else: print('Введите число!')
