x=input('Kod goroda:')
y=int(input('Dlitelnost razgovora:'))
z=0
if x=='343':
    z=y*15
elif x=='381':
    z=y*18
elif x=='473':
    z=y*13
elif x=='485':
    z=y*11
else:
    print('Ne suschestvuet!')
if z:
    print('Stoimost:',z)
    
    
