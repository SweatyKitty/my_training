import tkinter as tk


def count():
    int(number_1.get())

window=tk.Tk()
window.title("Калькулятор суммы для рассрочки")
window.geometry('600x450')
window.resizable(False,False)

button_3_month=tk.Button(window,width=12, height=3, text='3-10 м.')
button_3_month.place(x=24, y=250)

button_12_month=tk.Button(window,width=12, height=3, text='12-18')
button_12_month.place(x=173, y=250)

button_18_month=tk.Button(window,width=12, height=3, text='18-24')
button_18_month.place(x=322, y=250)

button_36_month=tk.Button(window,width=12, height=3, text='24-36')
button_36_month.place(x=471, y=250)

number1_entry=tk.Entry(window, width=90)
number1_entry.place(x=24, y=200)

window.mainloop()