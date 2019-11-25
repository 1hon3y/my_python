def str_n(s,n):
    x=int(n)
    if len(s)>x:
        return s.upper()
    else:
        return s

q=input('Введите строку:')
y=input('Введите число:')
print(f'Строка:{str_n(q,y)}')
