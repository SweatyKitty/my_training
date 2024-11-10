area=[['*','*','*'],['*','*','*'],['*','*','*']]
for i in area:
    print(*i)
cell_adress={1:[0,0],2:[0,1],3:[0,2],4:[1,0],5:[1,1],6:[1,2],7:[2,0],8:[2,1],9:[2,2]}
turn=0

def check_winner():
    if area[0][0]==area[1][0] and area[1][0]==area[2][0]:
        return area[0][0]
    elif area[0][1]==area[1][1] and area[1][1]==area[2][1]:
        return area[0][1]
    elif area[0][1] == area[1][1] and area[1][1] == area[2][1]:
        return area[0][1]
    elif area[0][2] == area[1][2] and area[1][2] == area[2][2]:
        return area[0][2]
    elif area[0][2] == area[1][1] and area[1][1] == area[2][0]:
        return area[0][2]
    elif area[0][0] == area[1][1] and area[1][1] == area[2][2]:
        return area[0][0]
    elif area[0][0] == area[0][1] and area[0][1] == area[0][2]:
        return area[0][0]
    elif area[1][0] == area[1][1] and area[1][1] == area[1][2]:
        return area[1][0]
    elif area[2][0] == area[2][1] and area[2][1] == area[2][2]:
        return area[2][0]
    else:
        return '*'

def draw_area():#Функция замены значений
    if turn_char=='X':
        area[row][collumn]='X'
    else:
        area[row][collumn] = '0'
    for i in area:
        print(*i)
    print()


print('Перед вами поле игры, представьте, что клетки пронумерованы как циферблат на кнопочном телефоне')

def input_module():
    a=input('1-9 сделать ход (0-выход): ')
    collumn , row= cell_adress.pop(int(a))
    return collumn,row


for turn in range(1,9):
    if turn%2==0:
        turn_char='0'
        turn_letter='Ходят нолики'
    else:
        turn_char='X'
        turn_letter='Ходят крестики'
    print(f'Ход №{turn}, {turn_letter}')
    row, collumn=input_module()
    draw_area()
    if turn>5:
        if check_winner()=="X":
            print('Победа Крестиков')
            break
        elif check_winner()=='0':
            print('Победа Ноликов')
            break
        elif check_winner()=='*':
            if turn==8:
                print('Ничья')
                break
            else:
                continue