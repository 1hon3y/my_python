lst=[]

def menu():
    print('''Простой todo:
    1)Добавить задачу
    2)Вывести список задач
    3)Выход
    ''')

def add_new():
    task=[]
    cat=[]
    t=input('Сформулируйте задачу:')
    task.append(t)
    c=input('Добавьте категорию:')
    task.append(c)
    time=input('Добавьте время:')
    task.append(time)
    lst.append(task)

def print_list():
    if lst==[]:
        print('Список пуст')
    else:
        for i in lst:
            print('Задача:',i[0],' Категория:',i[1],' Дата:',i[2])

while True:
    menu()
    q=input('Выберите пункт:')
    if q=='1':
        add_new()
    elif q=='2':
        print_list()
    elif q=='3':
        break
    else:
        print('Ошибка!')
