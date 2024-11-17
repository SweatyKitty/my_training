def find_max(list_):
    max=list_[0]
    for i in list_:
        if i>max:
            max=i
    return(max)
def count_even(list_):
    i=0
    for a in list_:
        if a%2==0:
            i+=1
    return(i)
