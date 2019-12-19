film = input('Выбрать фильм: ')
day = input('Выбрать день(сегодня, завтра): ')
time = input('Выбрать время: ')
count = input('Выбрать кол-во билетов: ')

films = {
    'Пятница': {
            12: 250,
            16: 350,
            20: 450
        },
    'Чемпионы': {
            10: 250,
            13: 350,
            16: 350
        },
    'Пернатая банда': {
            10: 350,
            14: 450,
            18: 450
        }
}

if film in films:
    time = int(time)
    
    if time in films[film]:
        
        if day == 'сегодня':
            sk = 0
        elif day == 'завтра':
            sk = 5
        else: print('Ошибка ввода')
        
        if count:
            count = int(count)
            if count >= 20:
                sk = sk + 20
            rez = count * films[film][time]*(100-sk)/100
            print(f'Результат:{rez} руб.')
        else: print('Ошибка ввода')
        
    else: print('Ошибка ввода')
    
else: print('Ошибка ввода')
