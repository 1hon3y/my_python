summa = 0

while True:
    a = input('Введите число или Стоп для выхода: ')
    if a.lower() == 'стоп':
        break
    else:
        if a.isdigit():
            summa += int(a)
        else:
            print('Ошибка ввода')
    
print(f'Сумма:{summa}')
