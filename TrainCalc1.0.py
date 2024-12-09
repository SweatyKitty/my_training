import tkinter as tk
def month_3():
    count(1,3)
def month_12():
    count(2,12)
def month_18():
    count(3,18)
def month_36():
    count(3,24)

def count(i=1,f=3):
    a=int(number1_entry.get())
    b=6*i
    if i==4:
        bb=b+4
    else:
        bb=b
    c=100-bb
    d=a/c
    l=round(d*100,2)
    z=round(l/f,2)
    answer_entry.delete(0, 'end')
    answer_entry.insert(0, l )
    answer_2_entry.delete(0,'end')
    answer_2_entry.insert(0, z)

def month_payment(i=1):
    a=float(answer_entry.get())
    b=round(a/i,2)
    answer_2_entry.delete(0, 'end')
    answer_2_entry.insert(0, b)
def dop_month_6():
    month_payment(6)
def dop_month_10():
    month_payment(10)
def dop_month_36():
    count(4.8,36)

window=tk.Tk()
window.title("Калькулятор суммы для рассрочки")
window.geometry('600x450')
window.resizable(False,False)

button3_title=tk.Label(window, text='Платеж рассчитан по первой цифре диапазона месяцев \n При необходимости уточните месяцы:')
button3_title.place(x=24, y=195)

button_3_month=tk.Button(window,width=12, height=3, text='от 3х до 10 \n месяцев', command=month_3)
button_3_month.place(x=24, y=230)

button_6_month=tk.Button(window,width=5, height=1, text='6м.', command=dop_month_6)
button_6_month.place(x=24, y=290)
button_10_month=tk.Button(window,width=5, height=1, text='10м.', command=dop_month_10)
button_10_month.place(x=73, y=290)

button_12_month=tk.Button(window,width=12, height=5, text='от 12 до 18\n месяцев',command=month_12)
button_12_month.place(x=173, y=230)

button_18_month=tk.Button(window,width=12, height=3, text='от 18 до 24\n месяцев',command=month_18)
button_18_month.place(x=322, y=230)

button_36_month=tk.Button(window,width=12, height=5, text='36\n месяцев',command=dop_month_36)
button_36_month.place(x=471, y=230)

button_36_2_month=tk.Button(window,width=12, height=1, text='24м.', command=month_36)#Используется для расчета 24 месяца
button_36_2_month.place(x=322, y=290)

number1_title=tk.Label(window, text='Введите сколько должен получить магазин:')
number1_title.place(x=24, y=160)


number1_entry=tk.Entry(window, width=90)
number1_entry.place(x=24, y=180)

number2_title=tk.Label(window, text='Сумма для указания на сайте с рассрочкой:')
number2_title.place(x=24, y=320)

answer_entry=tk.Entry(window, width=90)
answer_entry.place(x=24, y=340)

number3_title=tk.Label(window, text='Примерный платеж в месяц')
number3_title.place(x=24, y=380)

answer_2_entry=tk.Entry(window, width=90)
answer_2_entry.place(x=24, y=400)

window.mainloop()