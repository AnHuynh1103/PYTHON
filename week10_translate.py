from tkinter import *
import numpy as np
from tkinter.scrolledtext import ScrolledText

di = ['VIỆT','ANH']

def callback():
    global i
    if i == 0:
        lb1.configure(text = di[0])
        lb2.configure(text = di[1])
        text_1.delete(1.0,END)
        text_2.delete(1.0,END)
        i = 1
    elif i == 1:
        lb1.configure(text = di[1])
        lb2.configure(text = di[0])
        text_1.delete(1.0,END)
        text_2.delete(1.0,END)
        i = 0
    
def translate():
    global i,dict_1,dict_2,a,j
    a = text_1.get('1.0',"end-1c").lower()
    print(a)
    text_2.delete(1.0,END)
    if i == 0:
        for j in range(8):
            if a == dict_1[j]:
                text_2.insert(END,dict_2[j])
    elif i == 1:
        for j in range(8):
            if a == dict_2[j]:
                text_2.insert(END,dict_1[j])
        
    
root = Tk()
root.geometry('800x400')
root.title('Translate Tool')
#
i = 0
#
dict_1 = ['room','book','wall','shark','dog','cat','car','pig']
dict_2 = ['phòng','sách','tường','cá mập','chó','mèo','xe hơi','heo']
#
switch = Button(text = '<->', font=('Verdana', 10), command = callback) #add command
switch.place(x = 380, y = 10)

#
translate = Button(text = 'TRANSLATE', font=('Verdana', 16), command = translate) #add command
translate.place(x = 330, y = 280)

#
text_1 = ScrolledText(font=('Verdana', 16), height=4, width=16)
text_2 = ScrolledText(font=('Verdana', 16), height=4, width=16)

text_1.place(x = 140, y = 70)
text_2.place(x = 440, y = 70)

#
lb1 = Label(text='ANH', font=('Verdana', 24, 'bold'))
lb2 = Label(text='VIỆT', font=('Verdana', 24, 'bold'))

lb1.place(x = 200, y = 20)
lb2.place(x = 500, y = 20)
#

mainloop()