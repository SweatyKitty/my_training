import tkinter as tk
def month_3():
    count(1)
def month_12():
    count(2)
def month_18():
    count(3)
def month_36():
    count(4)

def count(i=1):
    a=int(number1_entry.get())
    b=6*i
    if i==4:
        bb=b+4
    else:
        bb=b
    c=100-bb
    d=a/c
    l=round(d*100,2)
    answer_entry.delete(0, 'end')
    answer_entry.insert(0, l )


window=tk.Tk()
window.title("Калькулятор суммы для рассрочки")
window.geometry('600x450')
window.resizable(False,False)

button_3_month=tk.Button(window,width=12, height=3, text='3-10 м.', command=month_3)
button_3_month.place(x=24, y=250)

button_12_month=tk.Button(window,width=12, height=3, text='12-18',command=month_12)
button_12_month.place(x=173, y=250)

button_18_month=tk.Button(window,width=12, height=3, text='18-24',command=month_18)
button_18_month.place(x=322, y=250)

button_36_month=tk.Button(window,width=12, height=3, text='24-36',command=month_36)
button_36_month.place(x=471, y=250)

number1_entry=tk.Entry(window, width=90)
number1_entry.place(x=24, y=200)

answer_entry=tk.Entry(window, width=90)
answer_entry.place(x=24, y=340)

window.mainloop()