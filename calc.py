from tkinter import *
window = Tk()

Label(text="Label 1", bg='red').grid(row=0, column=0, rowspan=2, sticky='ns')
Label(text="Label 2").grid(row=0, column=1)
Label(text="Label 3").grid(row=1, column=1)

t_m4 = Label(text="Label 4")
t_m4.grid(row=2, column=2)

t_m5 = Label(text="Label 5", bg='blue')
t_m5.grid(row=3, column=0, columnspan=3, sticky='we')

window.mainloop()
