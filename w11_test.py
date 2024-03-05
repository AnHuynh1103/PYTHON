from tkinter import *

di = ["USD","VND"]
def callback():
    global i
    if i == 0:
        USD.delete(1.0,END)
        VND.delete(1.0,END)
        USD.insert(END,di[0])
        VND.insert(END,di[1])
        lb4.configure(text=' ')
        i = 1
    elif i == 1:
        USD.delete(1.0,END)
        VND.delete(1.0,END)
        USD.insert(END,di[1])
        VND.insert(END,di[0])
        lb4.configure(text=' ')
        i = 0

def CONVERT():
    global temp,i,biendoi
    temp = float(amount.get())
    if i == 0:
            biendoi = round(temp/24835.366,3)
            biendoi = str(biendoi)
            lb4.configure(text=' ' + biendoi + " USD")
    elif i == 1:
            biendoi = round(temp*24835.366,3)
            biendoi = str(biendoi)
            lb4.configure(text = '' + biendoi + " VND")


def key(event):
    global temp,i,biendoi
    temp = float(amount.get())
    if i == 0:
        if event.keysym == "Return":
            biendoi = round(temp/24835.366,3)
            biendoi = str(biendoi)
            lb4.configure(text=' ' + biendoi + " USD")
    elif i == 1:
        if event.keysym == "Return":
            biendoi = round(temp*24835.366,3)
            biendoi = str(biendoi)
            lb4.configure(text = '' + biendoi + " VND")
        

#
i = 1
#
root = Tk()
root.geometry("800x400")

root.bind("<Return>" , key)
#
amount = Entry(font=('Verdana', 16),width=8)
USD = Text(font=('Verdana', 16), height=1, width=8)
VND = Text(font=('Verdana', 16), height=1, width=8)

amount.place(x = 100, y = 60)
USD.place(x = 300, y = 60)
VND.place(x = 500, y = 60)

USD.insert(END,di[0])
VND.insert(END,di[1])
#
lb1 = Label(text = "AMOUNT",font=('Verdana', 12))
lb2 = Label(text = "FROM",font=('Verdana', 12))
lb3 = Label(text = "TO",font=('Verdana', 12))

lb1.place(x = 100, y = 20)
lb2.place(x = 300, y = 20)
lb3.place(x = 500, y = 20)
#
switch = Button(text = '<->', font=('Verdana', 10), command = callback) #add command
switch.place(x = 430, y = 60)
#
con = Button(text = "CONVERT" , font=('Verdana', 10), command = CONVERT)
con.place(x = 450, y = 230)
#
lb4 = Label(text=' ',font=('Verdana', 10))
lb4.place(x=150,y=250)
#

mainloop()