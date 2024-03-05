from tkinter import *
from tkinter.scrolledtext import ScrolledText
def callback(self):
    lb1.configure(text=s.get())
    
root = Tk()
root.geometry('800x600')

s = IntVar()
scale = Scale(from_=0, to_=100, length=500, var = s, orient='horizontal',showvalue='YES',tickinterval=50,command=callback)
lb1 = Label(text=s.get(),font=('Verdana', 16))



scale.grid(row=0,column=1)
lb1.grid(row=1,column=1)



mainloop()