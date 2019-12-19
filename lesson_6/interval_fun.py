from operator import add
res=0
for x in range(10,31,2):
    res+=add(pow(x,2),3)
print(res)
