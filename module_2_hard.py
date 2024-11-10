import random
#a=random.choice(range(3,21))
a=20
print('Первое число: ',a)

The_key=[]
for i in range(1,a+1):
    for j in range(1,a+1):
        if a%(i+j)==0 and i!=j:
            if The_key.__contains__(int(f'{j}{i}'))==False and The_key.__contains__(int(f'{i}{j}'))==False:
                The_key.append(int(f'{i}{j}'))
                continue
            else:
                continue
        else:
            continue
print(The_key)