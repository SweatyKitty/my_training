oper=input('(//-для деления нацело, **-для возведения в степень)‘\nВведите математическую операцию для вычисления: ')
mathlist=['+','-','*','/','**','//']
#mathlist.extend(oper)
signpos=0
while oper[signpos].isnumeric()==True:
    signpos+=1

if oper[signpos+1]=='*' or oper[signpos+1]=='/':#Проверка не степень ли это или деление нацело
    Firstnumberdel = int(oper[0:signpos])
    Secondnuberdel = int(oper[signpos + 2:])
    if oper[signpos+1]=='*':
        print(Firstnumberdel**Secondnuberdel)
    else:
        print(Firstnumberdel//Secondnuberdel)

else:#если базовые функции
    Firstnumber=int(oper[0:signpos])
    Secondnuber=int(oper[signpos+1:])
    opnum0=0
    while mathlist[opnum0]!=oper[signpos] or opnum0==4:
        opnum0+=1
    if opnum0==0:
        print(Firstnumber+Secondnuber)
    if opnum0==1:
        print(Firstnumber-Secondnuber)
    if opnum0==2:
        print(Firstnumber*Secondnuber)
    if opnum0==3:
        print(Firstnumber/Secondnuber)