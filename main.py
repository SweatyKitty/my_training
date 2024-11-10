name=int(input('Введите ваше число: '))
a=str(name)
i=0
while len(a)!=1:
    i=len(a)-1
    b=0
    while i!=-1:
        b=b+int(a[i])
        i=i-1
    a=str(b)
if b==3 or b==6 or b==9:
    x=int(str(name)[-1])
    if x==0 or x==5:
        print('FizzBuzz')
    else:
        print('Fizz')
else:
    x = int(str(name)[-1])
    if x == 0 or x == 5:
        print('Buzz')
    else:
        print('None')