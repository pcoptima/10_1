import logic_calc as lc
from tkinter import *
from tkinter import ttk

first_num = 0
second_num = 0
operator = ''


def up_entry(num):
    e.insert(END, num)


def clear_entry():
    e.delete(0, END)


def rezult_calc():
    global second_num
    second_num = int(e.get())
    e.delete(0, END)
    if operator == "+":
        rez = lc.add(first_num, second_num)
    elif operator == "-":
        rez = lc.substruct(first_num, second_num)
    elif operator == "*":
        rez = lc.multiply(first_num, second_num)
    elif operator == "/":
        rez = lc.divide(first_num, second_num)
    e.insert(END, rez)


def choise_oper(oper):
    global first_num, operator
    first_num = int(e.get())
    operator = oper
    e.delete(0, END)


window = Tk()

e = Entry(window, width=20, font=('Arial', 14), justify="right")
e.grid(row=0, column=0, columnspan=4, sticky='ew')

sty = ttk.Style()
sty.configure('My.TButton', font=('Arial', 14))

b1 = ttk.Button(window, text='1',
                style='My.TButton', command=lambda: up_entry('1'))
b1.grid(row=1, column=0)
b2 = ttk.Button(window, text='2',
                style='My.TButton', command=lambda: up_entry('2'))
b2.grid(row=1, column=1)
b3 = ttk.Button(window, text='3',
                style='My.TButton', command=lambda: up_entry('3'))
b3.grid(row=1, column=2)
b4 = ttk.Button(window, text='4',
                style='My.TButton', command=lambda: up_entry('4'))
b4.grid(row=2, column=0)
b5 = ttk.Button(window, text='5',
                style='My.TButton', command=lambda: up_entry('5'))
b5.grid(row=2, column=1)
b6 = ttk.Button(window, text='6',
                style='My.TButton', command=lambda: up_entry('6'))
b6.grid(row=2, column=2)
b7 = ttk.Button(window, text='7',
                style='My.TButton', command=lambda: up_entry('7'))
b7.grid(row=3, column=0)
b8 = ttk.Button(window, text='8',
                style='My.TButton', command=lambda: up_entry('8'))
b8.grid(row=3, column=1)
b9 = ttk.Button(window, text='9',
                style='My.TButton', command=lambda: up_entry('9'))
b9.grid(row=3, column=2)
b0 = ttk.Button(window, text='0',
                style='My.TButton', command=lambda: up_entry('0'))
b0.grid(row=4, column=0)

b_add = ttk.Button(window, text='+',
                   style='My.TButton', command=lambda: choise_oper('+'))
b_add.grid(row=1, column=3)
b_sub = ttk.Button(window, text='-',
                   style='My.TButton', command=lambda: choise_oper('-'))
b_sub.grid(row=2, column=3)
b_mul = ttk.Button(window, text='*',
                   style='My.TButton', command=lambda: choise_oper('*'))
b_mul.grid(row=3, column=3)
b_de = ttk.Button(window, text='/',
                  style='My.TButton', command=lambda: choise_oper('/'))
b_de.grid(row=4, column=3)


b_clear = ttk.Button(window, text='C',
                     style='My.TButton', command=clear_entry)
b_clear.grid(row=4, column=1)
b_rez = ttk.Button(window, text='=',
                   style='My.TButton', command=rezult_calc)
b_rez.grid(row=4, column=2)


window.mainloop()
