from tkinter import *
def callback(x):
    global operator
    l3.configure(text='{}'.format(pt[x]))
    operator = pt[x]
    
def nutAC():
    global operator
    l3.configure(text='')
    l4.configure(text='')
    E1.delete(0, END)
    E2.delete(0, END)
    E3.delete(0, END)
    operator = 0

def daubang():
	global operator
	s1 = E1.get()
	s2 = E2.get()
	E3.delete(0,END)

	if operator==0:
		l4.configure(text="Enter operator")
	else:
		l4.configure(text="")
		if operator=='/' and s2=='0':
			l4.configure(text="Number 2 must not be 0")
		else:
			E3.insert(0, eval(s1+operator+s2))
                
root = Tk()
root.geometry("800x600")
root.title("Calculator")

l1 = Label(text='Number 1', font=('Verdana', 24, 'bold'))
l2 = Label(text='Number 2', font=('Verdana', 24, 'bold'))
l3 = Label(text='', font=('Verdana', 24, 'bold'))
l4 = Label(text='', font=('Verdana', 24, 'bold'))

E1 = Entry(font=('Verdana', 24, 'bold'),width = 5)
E2 = Entry(font=('Verdana', 24, 'bold'),width = 5)
E3 = Entry(font=('Verdana', 24, 'bold'),width = 5)
pt = '+-*/'

operator = 0
buttons = [0]*4 # create a list to hold 4 buttons

for i in range(4):
    buttons[i] = Button(text=pt[i], font=('Verdana', 24, 'bold'), command = lambda x=i: callback(x))
    buttons[i].grid(row=2, column=i)
    
daubang = Button(text='=', font=('Verdana', 24, 'bold'), command = daubang)
AC = Button(text='AC', font=('Verdana', 24, 'bold'),command = nutAC)

l1.grid(row=0, column=0)
l2.grid(row=0, column=2)
l3.grid(row=1, column=1)
l4.grid(row=5, column=0, columnspan=3)


daubang.grid(row=3,column=1)
AC.grid(row=3,column=2)
E1.grid(row=1, column=0)
E2.grid(row=1, column=2)
E3.grid(row=4, column=1)


mainloop()

'''from tkinter import *

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
root = Tk()

#cheetah_image = PhotoImage(file='test_01.png')

button_frame = Frame()
buttons = [0]*26
for i in range(26):
    buttons[i] = Button(button_frame, text=alphabet[i])
    buttons[i].grid(row=0, column=i)
    
ok_button = Button(text='Ok', font=('Verdana', 24))

button_frame.grid(row=0, column=0)
ok_button.grid(row=1, column=0)
mainloop()'''

'''from tkinter import *

root = Tk()

canvas = Canvas(width=200,height=200,bg='white')


#canvas.create_rectangle(20,20,120,120,fill='red')
#canvas.create_oval(20,20,100,100, fill='blue')
#canvas.create_line(20,100,70,180, fill='green')


canvas.grid(row=0,column=0)
mainloop()'''