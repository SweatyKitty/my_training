import tkinter as tk
from tkinter import Button, Entry
def gen_check():
    if i is list:
        list_check(u)
    elif i is dict:
        dict_check(u)
    elif i is tuple:
        tuple_check()
    elif i is set:
        set_check()
    else:
        int_float_String_bool_check()

def list_check(u):

def dict_check(u):
    a=[*u]
    z=0
    for i in range(len(u)):
        z=z+len(a[i])+int(u[a[i]])+1
    return(z)


def tuple_check(u):

def set_check(u):

def int_float_String_bool_check():

def count():
    data_structure=[string_Entry.get()]
    for i in data_structure:
        isinstance()

window=tk.Tk()
window.title('Окно для задачи хард 3 модуля')
window.geometry('700x400')
window.resizable(False, False)

button_count=tk.Button(window,width=10, height=10, text='3-10 м.', command=count)
button_count.place(x=335, y=250)

string_Entry=tk.Entry(window, width=90)
string_Entry.place(x=40, y=200)

string_Entry=tk.Entry(window, width=90)
string_Entry.place(x=40, y=310)

window.mainloop()