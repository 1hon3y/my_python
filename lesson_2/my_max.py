def my_max(x,y):
    if x>y:
        return x + ' больше'
    elif x<y:
        return y + ' больше'
    else:
        return 'Они равны'
    
print(my_max(input('Введите 1 число:\n'),input('Введите 2 число:\n')))
