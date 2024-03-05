'''from tkinter import *
WD = Tk ()
WD2 = Tk()
WD.title("222")
WD.mainloop()
WD2.title("cc")
WD2.mainloop()'''

'''from tkinter import *
parent = Tk()
B1 = Button(parent, text = "Red", fg = "red")
B1.pack(side = LEFT)
B2 = Button(parent, text = "Black", fg = "black")
B2.pack(side = RIGHT)
B3 = Button(parent, text = "Blue", fg = "blue")
B3.pack(side = TOP)
B4 = Button(parent, text = "Green", fg = "green")
B4.pack(side = BOTTOM)
parent.mainloop()'''

'''from tkinter import *
parent = Tk()
T1 = Label(parent, text = "Name").grid(row = 0, column = 0)
e1 = Entry(parent).grid(row = 0, column = 1)
T2 = Label(parent, text = "Password").grid(row = 1, column = 0)
e2 = Entry(parent).grid(row = 1, column = 1)
B1 = Button(parent, text = "Submit").grid(row = 4, column = 0)
parent.mainloop()'''

'''from tkinter import *
top = Tk()
top.geometry("300x200")
T1 = Label(top, text = "Name").place(x = 30, y = 50)
T2 = Label(top, text = "Email").place(x = 30, y = 90)
T3 = Label(top, text = "Password").place(x = 30, y = 130)
E1 = Entry(top).place(x = 100, y = 50)
E2 = Entry(top).place(x = 100, y = 90)
E3 = Entry(top).place(x = 100, y = 130)
top.mainloop()'''

'''from tkinter import *
def callback():
    a = e1.get()
    l1.configure(text = "APEN", bg = "white", fg ="black")
    l2.configure(text = a, fg = "red")
    l3.configure(bg="green")
    e1.invert(2, "hello")
root = Tk()
root.title('Oh shiet')
root.geometry('900x600')
l1 = Label(root, text = "Applying Programing\n For Engineering", font = ('Times New Roman', 24), fg = "black", bg = "white")
l1.grid(row=0,column=0,columnspan=2)
l2 = Label(root, text = "Chapter 1", font = ('Times New Roman', 24), fg = "black", bg = "white")
l2.grid(row=1,column=0)
l3 = Label(root, text = "Chapter 2", font = ('Times New Roman', 24), fg = "black", bg = "white")
l3.grid(row=2,column=0)
e1 = Entry(font=("Arial", 50), width=24,)
e1.grid(row=3,column=0,columnspan=2)
b1 = Button(root, text = "Submit", font=("Times", 24))
b1.grid(row=4,column=0,columnspan=2)
mainloop()'''

'''from tkinter import *
def calculate():
    temp = int(entry.get())
    temp = 9/5*temp+32
    output_label.configure(text = 'Converted: {:.1f}'.format(temp))
    entry.delete(0,END)
root = Tk()
root.geometry("400x400")
message_label = Label(text='Enter a temperature',font=('Verdana', 16))
output_label = Label(font=('Times', 20))
entry = Entry(font=('Times', 20), width=4)
calc_button = Button(text='Ok', font=('Times', 20),command=calculate)
message_label.grid(row=0, column=0)
entry.grid(row=0, column=1)
calc_button.grid(row=0, column=2)
output_label.grid(row=1, column=0, columnspan=3)
mainloop()'''

'''from tkinter import *
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
def callback(x):
    label.configure(text='Button {} clicked'.format(alphabet[x]))
root = Tk()
label = Label()
label.grid(row=1, column=0, columnspan=26)
buttons = [0]*26 # create a list to hold 26 buttons
for i in range(26):
    buttons[i] = Button(text=alphabet[i],
        command = lambda x=i: callback(x))
    buttons[i].grid(row=0, column=i)
mainloop()'''

'''from tkinter import *
def callback(r,c):
    global player
    if player == 'X':
        b[r][c].configure(text = 'X')
        player = 'O'
    else:
        b[r][c].configure(text = 'O')
        player = 'X'
root = Tk()
b = [[0,0,0],       
    [0,0,0],
    [0,0,0]]
for i in range(3):
    for j in range(3):
        b[i][j] = Button(font=('Verdana', 56), width=3, bg='yellow',
            command = lambda r=i,c=j: callback(r,c))
        b[i][j].grid(row = i, column = j)
player = 'X'
mainloop()'''



