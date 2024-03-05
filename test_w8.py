from tkinter import *
def callback():
    show_totals.get()
    a = color.get()
    if a == 1:
        show_totals
    
root = Tk()
root.geometry('800x600')

show_totals = IntVar()
show_totals.set(0) #set gia tri ban dau cua nut check la 1 hoac 0
check = Checkbutton(text='Show totals', var=show_totals,command=callback)

color = IntVar()
redbutton = Radiobutton(text='Red', var=color, value=1,command=callback)
greenbutton = Radiobutton(text='Green', var=color, value=2,command=callback)
bluebutton = Radiobutton(text='Blue', var=color, value=3,command=callback)

check.grid(row=0,column=0)
redbutton.grid(row=1,column=0)
greenbutton.grid(row=1,column=1)
bluebutton.grid(row=1,column=2)


show_totals.get()
mainloop()