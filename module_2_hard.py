import random
a=random.choice(range(3,21))
print('Заданное число: ',a)

The_key=[]
for i in range(1,a+1):
    for j in range(1,a+1):
        if a%(i+j)==0 and i!=j:
            if The_key.__contains__([j,i])==False and The_key.__contains__([i,j])==False:
                The_key.append([i,j])
                continue
            else:
                continue
        else:
            continue
# print(The_key)
The_Final_Key=''
for k in range(len(The_key)):
    The_Final_Key=The_Final_Key+str(The_key[k][0])
    The_Final_Key = The_Final_Key + str(The_key[k][1])
print(f'Подобранный пароль: {The_Final_Key}')