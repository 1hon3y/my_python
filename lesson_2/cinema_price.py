print('Программа для подсчёта стоимости билетов в кино.')

film=input('Выберите фильм:')
date=input('Выберите дату(сегодня, завтра):')
time=int(input('Выберите время:'))
count=int(input('Выберите количество билетов:'))

print('Выбрали фильм:',film,' День:',date,' Время:',time,' Кол-во билетов:',count)

x=None

if film == 'Пятница':
    if time == 12:
        x=250
    elif time == 16:
        x=350
    elif time == 20:
        x=450
        
        
elif film == 'Чемпионы':
    if time == 10:
        x=250
    elif time == 13:
        x=350
    elif time == 16:
        x=350

elif film == 'Пернатая банда':
    if time == 10:
        x=350
    elif time == 14:
        x=450
    elif time == 18:
        x=450     
    
if x:    
    if date=='сегодня':
        sk=0
    elif date=='завтра':
        sk=5
    else:
        sk=1
        print('Ошибка ввода')

    if sk !=1:
        if count:
            if count>=20:
                sk+=20
            rez=x*count*(100-sk)/100
            print('Результат: ',rez,' руб.')
        else:
            print('Ошибка ввода')
else:
    print('Ошибка ввода')

        
