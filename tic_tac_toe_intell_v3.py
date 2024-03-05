from tkinter import *
import random

def callback(r,c):
    global player
    if player == 'X' and states[r][c] == 0 and stop_game==False:
        b[r][c].configure(text='X', fg='blue', bg='white')
        states[r][c] = 'X'
        player = 'O'
    check_for_winner()
    while states[r][c]!=0 and stop_game==False:
        if states[1][1] == 0:
            r = 1
            c = 1
        elif states[0][0] == states[1][0] == 'O': ###case 1 col 0
            if  states[2][0] == 0:
                r = 2
                c = 0
            else:
                r = random.randint(0,2)
                c = random.randint(0,2)
        elif states[1][0] == states[2][0] == 'O': ###case 2 col 0
            if  states[0][0] == 0:
                r = 0
                c = 0
            else:
                r = random.randint(0,2)
                c = random.randint(0,2)
        elif states[2][0] == states[0][0] == 'O': ###case 3 col 0
            if  states[1][0] == 0:
                r = 1
                c = 0
            else:
                r = random.randint(0,2)
                c = random.randint(0,2)
        #####################
        #####################
        elif states[0][1] == states[1][1] == 'O': ###case 1 col 1
            if  states[2][1] == 0:
                r = 2
                c = 1
            else:
                r = random.randint(0,2)
                c = random.randint(0,2)
        elif states[1][1] == states[2][1] == 'O': ###case 2 col 1
            if  states[0][1] == 0:
                r = 0
                c = 1
            else:
                r = random.randint(0,2)
                c = random.randint(0,2)
        elif states[2][1] == states[0][1] == 'O': ###case 3 col 1
            if  states[1][1] == 0:
                r = 1
                c = 1
            else:
                r = random.randint(0,2)
                c = random.randint(0,2)
        #####################
        #####################
        elif states[0][2] == states[1][2] == 'O': ###case 1 col 2
            if  states[2][2] == 0:
                r = 2
                c = 2
            else:
                r = random.randint(0,2)
                c = random.randint(0,2)
        elif states[1][2] == states[2][2] == 'O': ###case 2 col 2
            if  states[0][2] == 0:
                r = 0
                c = 2
            else:
                r = random.randint(0,2)
                c = random.randint(0,2)
        elif states[2][2] == states[0][2] == 'O': ###case 3 col 2
            if  states[1][2] == 0:
                r = 1
                c = 2
            else:
                r = random.randint(0,2)
                c = random.randint(0,2)
        #####################
        #####################
        elif states[0][0] == states[0][1] == 'O': ###case 1 row 0
            if  states[0][2] == 0:
                r = 0
                c = 2
            else:
                r = random.randint(0,2)
                c = random.randint(0,2)
        elif states[0][2] == states[0][1] == 'O': ###case 2 row 0
            if  states[0][0] == 0:
                r = 0
                c = 0
            else:
                r = random.randint(0,2)
                c = random.randint(0,2)
        elif states[0][0] == states[0][2] == 'O': ###case 3 row 0
            if  states[0][2] == 0:
                r = 0
                c = 2
            else:
                r = random.randint(0,2)
                c = random.randint(0,2)
        #####################
        #####################
        elif states[1][0] == states[1][1] == 'O': ###case 1 row 1
            if  states[1][2] == 0:
                r = 1
                c = 2
            else:
                r = random.randint(0,2)
                c = random.randint(0,2)
        elif states[1][1] == states[1][2] == 'O': ###case 2 row 1
            if  states[1][0] == 0:
                r = 1
                c = 0
            else:
                r = random.randint(0,2)
                c = random.randint(0,2)
        elif states[1][0] == states[1][2] == 'O': ###case 3 row 1
            if  states[1][1] == 0:
                r = 1
                c = 1
            else:
                r = random.randint(0,2)
                c = random.randint(0,2)
        #####################
        #####################
        elif states[2][0] == states[2][1] == 'O': ###case 1 row 2
            if  states[2][2] == 0:
                r = 2
                c = 2
            else:
                r = random.randint(0,2)
                c = random.randint(0,2)
        elif states[2][2] == states[2][1] == 'O': ###case 2 row 2
            if  states[2][0] == 0:
                r = 2
                c = 0
            else:
                r = random.randint(0,2)
                c = random.randint(0,2)
        elif states[2][0] == states[2][2] == 'O': ###case 3 row 2
            if  states[2][1] == 0:
                r = 2
                c = 1
            else:
                r = random.randint(0,2)
                c = random.randint(0,2)
        #####################
        #####################
        elif states[0][0] == states[1][1] == 'O': ###case 1 cross 1
            if  states[2][2] == 0:
                r = 2
                c = 2
            else:
                r = random.randint(0,2)
                c = random.randint(0,2)
        elif states[2][2] == states[1][1] == 'O': ###case 2 cross 1
            if  states[0][0] == 0:
                r = 0
                c = 0
            else:
                r = random.randint(0,2)
                c = random.randint(0,2)
        elif states[0][0] == states[2][2] == 'O': ###case 3 cross 1
            if  states[1][1] == 0:
                r = 1
                c = 1
            else:
                r = random.randint(0,2)
                c = random.randint(0,2)
        #####################
        #####################
        elif states[0][2] == states[1][1] == 'O': ###case 1 cross 2
            if  states[2][0] == 0:
                r = 2
                c = 0
            else:
                r = random.randint(0,2)
                c = random.randint(0,2)
        elif states[2][0] == states[1][1] == 'O': ###case 2 cross 2
            if  states[0][2] == 0:
                r = 0
                c = 2
            else:
                r = random.randint(0,2)
                c = random.randint(0,2)
        elif states[2][0] == states[0][2] == 'O': ###case 3 cross 2
            if  states[1][1] == 0:
                r = 1
                c = 1
            else:
                r = random.randint(0,2)
                c = random.randint(0,2)
        else:
            r = random.randint(0,2)
            c = random.randint(0,2)
        #####################
        #####################
        '''for i in range(3):
            if states[0][i] == states[1][i] == 'O':
                r = 2
                c = i
            elif states[1][i] == states[2][i] == 'O':
                r = 0
                c = i
            elif states[2][i] == states [0][i] == 'O':
                r = 1
                c = i'''
        
       
    print('row:',r)
    print('col:',c) 
    if player == 'O' and stop_game==False:
        b[r][c].configure(text='O', fg='orange', bg='black')
        states[r][c] = 'O'
        player = 'X'
    check_for_winner()
    
def check_for_winner():
    global stop_game
    for i in range(3):
        if states[i][0]==states[i][1]==states[i][2]!=0:
            b[i][0].configure(bg='grey')
            b[i][1].configure(bg='grey')
            b[i][2].configure(bg='grey')
            stop_game = True
            
    for i in range(3):
        if states[0][i]==states[1][i]==states[2][i]!=0:
            b[0][i].configure(bg='grey')
            b[1][i].configure(bg='grey')
            b[2][i].configure(bg='grey')
            stop_game = True
            
        if states[0][0]==states[1][1]==states[2][2]!=0:
            b[0][0].configure(bg='grey')
            b[1][1].configure(bg='grey')
            b[2][2].configure(bg='grey')
            stop_game = True
            
        if states[2][0]==states[1][1]==states[0][2]!=0:
            b[2][0].configure(bg='grey')
            b[1][1].configure(bg='grey')
            b[0][2].configure(bg='grey')
            stop_game = True
        
        if get_open_spots() == { }:
            stop_game = True
          

def get_open_spots():
    return [[r,c] for r in range(3) for c in range(3) if states[r][c]==0]
 
def button():
    global b
    global stop_game
    global player
    global states
    for i in range(3):
        for j in range(3):
            b[i][j].configure(text = ' ', bg = "yellow")
            b[i][j].grid(row = i, column = j)
    states = [[0,0,0],
              [0,0,0],
              [0,0,0]]
    player = 'X'
    stop_game = False

root = Tk()
root.title('Tic Tac Toe')
b = [[0,0,0],
     [0,0,0],
     [0,0,0]]
states = [[0,0,0],
          [0,0,0],
          [0,0,0]]

reset_button = Button(text = 'RESET', font=('Verdana', 24, 'bold'),command=button)
reset_button.grid(row=1, column=4)

for i in range(3):
    for j in range(3):
        b[i][j] = Button(font=('Verdana', 56), width=3, bg='yellow',
                         command = lambda r=i,c=j: callback(r,c))
        b[i][j].grid(row = i, column = j)
        
player = 'X'
com1 = ' '
stop_game = False

mainloop()