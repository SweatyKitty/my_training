from itertools import count
from operator import truediv

data_structure = [[1, 2, 3], {'a': 4, 'b': 5}, (6, {'cube': 7, 'drum': 8}), "Hello", ((), [{(2, 'Urban', ('Urban2', 35))}])]


def calculate_structure_sum(data_str=[1,0,1]):
    if isinstance(data_str, int) == True:
        count_int(data_str)
    elif isinstance(data_str, str) == True:
        count_str(data_str)
    elif isinstance(data_str, dict) == True:
        count_list(params_dict(**data_str))
    elif isinstance(data_str, set) == True:
        count_list(count_set(data_str))
    else:
        for i in range(len(data_str)):
            if isinstance(data_str[i],list)==True:
                count_list(data_str[i])
            elif isinstance(data_str[i],dict)==True:
                count_list(params_dict(**data_str[i]))
            elif isinstance(data_str[i], tuple) == True:
                count_list(list(data_str[i]))
            elif isinstance(data_str[i], int) == True:
                count_int(data_str[i])
            elif isinstance(data_str[i], str) == True:
                count_str(data_str[i])
            elif isinstance(data_str[i], set) == True:
                count_list(count_set(data_str[i]))
        return(x)



x=0

def params_dict(**kwargs):
    b = []
    for key, value in kwargs.items():
        b.append(key)
        b.append(value)
    return(b)
def count_int(q=0):
    global x
    x=x+q

def count_str(w=''):
    global x
    x=x+len(w)

def count_list(e_e=[1,0,1]):
    for c in range(len(e_e)):
        calculate_structure_sum(e_e[c])
def count_set(mn):
    p=list(mn)
    return p

# print(range(len(data_structure)))
calculate_structure_sum(data_structure)
print(x)
