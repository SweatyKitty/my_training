import tkinter as tk
from tkinter import Button, Entry

def list_check():

def dict_check():

def tuple_check():

def set_check():

def int_float_String_bool_check():

def count():
    data_structure=[string_Entry.get()]
    for i in data_structure:


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