import random as ra
from random import random, randrange
def cpn(b=[1,1,1,1,1,1,1,1,1]):
    z=0
    while z<9:
        z=z+1
        a=b[z-1]
        #a=randrange(0,9)
        if z==1:
            answer='(9'
        elif z==3:
            answer=answer+') '
        elif z==6:
            answer = answer + '-'
        answer=answer+str(a)
    print(answer)
c=input("Введите 9 чисел: ")
b=list(c)
cpn(b)