from tkinter import *
def callback():
    global temp,a
    temp = int(entry.get())
    a = val.get()


def EXCHANGE():
    global temp,a
    temp = int(entry.get())
    a = val.get()
    if a == 1:
        usd = temp*22000
        usd = str(usd)
        lb1.configure(text=('Gia tri quy doi: '+ usd +' vnd'), fg='#f00')
        lb2.configure(text=' ')
    elif a == 2:
        eur = temp*26000
        eur = str(eur)
        lb1.configure(text=('Gia tri quy doi: ' + eur +' vnd'), fg='#f00')
        lb2.configure(text=' ')
    elif a == 3:
        jyp = temp*200
        jyp = str(jyp)
        lb1.configure(text=('Gia tri quy doi: '+ jyp +' vnd'), fg='#f00')
        lb2.configure(text=' ')
    else:
       lb2.configure(text='Vui long chon ngoai te!') 



def CLEAR():
    global temp,a,val
    temp = entry.get()
    lb1.configure(text=('Gia tri quy doi: 0 vnd'))
    lb2.configure(text=' ')
    entry.delete(0, END)
    val.set(0)

    
    
root = Tk()
root.geometry('400x400')

val = IntVar()
USD = Radiobutton(text='USD: 22.000',var = val,  value=1,font=('Verdana', 10),command=callback)
EUR = Radiobutton(text='EUR: 26.000',var = val,  value=2,font=('Verdana', 10),command=callback)
JYP = Radiobutton(text='JYP: 200',var = val,  value=3,font=('Verdana', 10),command=callback)



USD.place(x=50,y=50)
EUR.place(x=50,y=80)
JYP.place(x=50,y=110)


entry = Entry(font=('Verdana', 10, 'bold'),width = 10)
entry.place(x=250,y=50)


lb1 = Label(text=('Gia tri quy doi: 0 vnd'), fg='#f00',font=('Verdana', 8))
lb1.place(x=150,y=200)

lb2 = Label(text=' ',font=('Verdana', 8))
lb2.place(x=150,y=250)


exchange = Button(text='Exchange',font=('Verdana', 10),command=EXCHANGE)
exchange.place(x=250,y=100)

clear = Button(text='Clear',font=('Verdana', 10),command=CLEAR)
clear.place(x=250,y=150)


mainloop()