from tkinter import *
from tkinter.scrolledtext import ScrolledText
def callback(self):
    show_totals.get()
    a = color.get()
    if a == 1:
        show_totals
    lb1.configure(text=s.get())
    

"""def callback(event):
    print(event.keysym)"""



root = Tk()
root.geometry('800x600')

color0= IntVar()
color1= IntVar()
color2= IntVar()

show_totals = IntVar()
show_totals.set(0) #set gia tri ban dau cua nut check la 1 hoac 0
check = Checkbutton(text='Show totals', var=show_totals,command=callback)


"""root.bind('<Key>', callback)"""

textbox = ScrolledText(font=('Verdana', 16), height=6, width=40,undo=True)
s = IntVar()
scale = Scale(from_=0, to_=100,length=500,var=s, orient='horizontal',showvalue='YES',tickinterval=50,command=callback)
lb1 = Label(text=s.get(),font=('Verdana', 16))

color = IntVar()
redbutton = Radiobutton(text='Red', var=color, value=1,command=callback)
greenbutton = Radiobutton(text='Green', var=color, value=2,command=callback)
bluebutton = Radiobutton(text='Blue', var=color, value=3,command=callback)



textbox.grid(row=1,column=3)
scale.grid(row=2,column=3)

check.grid(row=0,column=0)
redbutton.grid(row=1,column=0)
greenbutton.grid(row=1,column=1)
bluebutton.grid(row=1,column=2)
lb1.grid(row=3,column=3)

show_totals.get()
mainloop()