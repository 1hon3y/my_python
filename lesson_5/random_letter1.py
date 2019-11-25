import random

def vybor_bukvy(lst):
    x=lst[random.randint(0,len(lst)-1)]
    w=list(x)
    y=random.randint(0,len(w))
    z=w[y]
    w[y]='?'
    q=''.join(w)
    return q,z,x

spisok=['магазин','строка','ремонт','учёба','логика','школа']
slovo_bukva=vybor_bukvy(spisok)
print(slovo_bukva[0])
user_bukva=input('Введите букву:')
if slovo_bukva[1]==user_bukva:
    print('Победа!')
else:
    print('Увы! Попробуйте ещё раз!')
print(f'Слово:{slovo_bukva[2]}!')
