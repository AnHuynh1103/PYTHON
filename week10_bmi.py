from tkinter import *

def callback():
    global temp_1,temp_2,a
    temp_1 = entry_1.get()
    temp_2 = entry_2.get()
        
    a = val.get()
    if a == 1:
        lb1.configure(text = 'Chiều cao (cm)')
        lb2.configure(text = 'Cân nặng (kg)')

    elif a == 2:
        lb1.configure(text = 'Chiều cao (inches)')
        lb2.configure(text = 'Cân nặng (pounds)')

def BMI():
    global a,temp_1,temp_2,high,weight,bmi
    temp_1 = entry_1.get()
    temp_2 = entry_2.get()
    
    if temp_1 == "":
            lb4.configure(text = 'Vui lòng nhập đầy đủ số liệu!',fg = '#f00')
            lb5.configure(text ='')
            lb4.place(x = 75, y = 310)
            lb3.configure(text ='BMI =')

    if temp_2 == "":
        temp_1 = ""
        if temp_1 == "":
            lb4.configure(text = 'Vui lòng nhập đầy đủ số liệu!', fg = '#f00')
            lb5.configure(text ='')
            lb4.place(x = 75, y = 310)
            lb3.configure(text ='BMI =')
    
    if temp_1 != "":
        temp_1 = float(temp_1)
        lb4.configure(text = '')
    
    if temp_2 != "" and temp_1 != "":
        temp_2 = float(temp_2)
        lb4.configure(text = '')
    
    if temp_1 == 0:
            lb4.configure(text = 'Không thể tính! Vui lòng nhập đúng!',fg = '#00f')
            lb5.configure(text ='')
            lb4.place(x = 60, y = 310)
            lb3.configure(text ='BMI =')
    
    if temp_2 == 0:
        temp_1 = 0
        if temp_1 == 0:
            lb4.configure(text = 'Không thể tính! Vui lòng nhập đúng!',fg = '#00f')
            lb5.configure(text ='')
            lb4.place(x = 60, y = 310)
            lb3.configure(text ='BMI =')
        
    
    a = val.get()
    if a == 1:
        high = temp_1/100
        weight = temp_2
        bmi = round(weight/(high*high),2)
        bmi = str(bmi)
        lb3.configure(text ='BMI = ' + bmi)
        solieu = float(bmi)
        if solieu < 18.5:
            lb5.configure(text = 'BMI cho thấy bạn thiếu cân cấp độ I!',fg='#00f')
        elif 18.5 <= solieu < 25:
            lb5.configure(text = 'Chúc mừng, bạn có BMI bình thường',fg='#080')
        elif 25 <= solieu < 30:
            lb5.configure(text = 'BMI trên bình thường, bạn thừa cân!',fg='#f00')
        elif 30 <= solieu < 35:
            lb5.configure(text = 'BMI cho thấy bạn béo phì cấp độ I!',fg='#f00')
        elif 35 <= solieu < 40:
            lb5.configure(text = 'BMI cho thấy bạn béo phì cấp độ II!',fg='#f00')
        else:
            lb5.configure(text = 'BMI cho thấy bạn béo phì cấp độ III! ',fg='#f00')
        lb4.configure(text =' ')
    elif a == 2:
        high = temp_1
        weight = temp_2
        bmi = round((weight/(high*high))*703,2)
        bmi = str(bmi)
        lb3.configure(text ='BMI = ' + bmi)
        solieu = float(bmi)
        if solieu < 18.5:
            lb5.configure(text = 'BMI cho thấy bạn thiếu cân cấp độ I!',fg='#00f')
        elif 18.5 <= solieu < 25:
            lb5.configure(text = 'Chúc mừng, bạn có BMI bình thường',fg='#080')
        elif 25 <= solieu < 30:
            lb5.configure(text = 'BMI trên bình thường, bạn thừa cân!',fg='#f00')
        elif 30 <= solieu < 35:
            lb5.configure(text = 'BMI cho thấy bạn béo phì cấp độ I!',fg='#f00')
        elif 35 <= solieu < 40:
            lb5.configure(text = 'BMI cho thấy bạn béo phì cấp độ II!',fg='#f00')
        else:
            lb5.configure(text = 'BMI cho thấy bạn béo phì cấp độ III! ',fg='#f00')
        lb4.configure(text =' ')
    else:
       lb4.configure(text = 'Hãy chọn loại đơn vị đo!')

def CLEAR():
    global val,bmi
    entry_1.delete(0, END)
    entry_2.delete(0, END)
    lb1.configure(text = 'Chiều cao')
    lb2.configure(text = 'Cân nặng')
    lb3.configure(text='BMI =')
    lb4.configure(text = ' ')
    lb5.configure(text = ' ')
    bmi = 0
    val.set(0)

#Create window
root = Tk()
root.geometry('400x400')
root.title('BMI CALCULATOR')

#Create button and place
val = IntVar()
metric = Radiobutton(text='Metric',var = val,  value=1,font=('Verdana', 10),command=callback)
english = Radiobutton(text='English',var = val,  value=2,font=('Verdana', 10),command=callback)

metric.place(x=200,y=50)
english.place(x=200,y=80)


#Create Label High and EntryBox
lb1 = Label(text=('Chiều cao'),font=('Verdana', 12))
lb1.place(x=20,y=30)

entry_1 = Entry(font=('Verdana', 10, 'bold'),width = 10)
entry_1.place(x=20,y=60)

#Create Label Weight and EntryBox
lb2 = Label(text='Cân nặng',font=('Verdana', 12))
lb2.place(x=20,y=100)

entry_2 = Entry(font=('Verdana', 10, 'bold'),width = 10)
entry_2.place(x=20,y=130)

#Create Button Calculate
cal = Button(text='Calculate',font=('Verdana', 12),command=BMI)
cal.place(x=120,y=200)

clear = Button(text='Clear',font=('Verdana', 12),command=CLEAR)
clear.place(x=220,y=200)

#

lb3 = Label(text = 'BMI =',font=('Verdana', 12))
lb3.place(x = 150 , y = 280)

#

lb4 = Label(text = ' ',font=('Verdana', 12))
lb4.place(x = 75 , y = 310)

#
lb5 = Label(text = ' ',font=('Verdana', 12))
lb5.place(x = 57 , y = 350)


mainloop()