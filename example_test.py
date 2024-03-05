import tkinter as tk
import random

def check_winner(board):
    # Check rows and columns
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != '':
            return board[i][0]  # Row winner
        if board[0][i] == board[1][i] == board[2][i] != '':
            return board[0][i]  # Column winner

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != '':
        return board[0][0]  # Diagonal winner
    if board[0][2] == board[1][1] == board[2][0] != '':
        return board[0][2]  # Diagonal winner

    return None

def is_board_full(board):
    for row in board:
        if '' in row:
            return False  # There is an empty space
    return True  # Board is full

def is_valid_move(board, row, col):
    return board[row][col] == ''

def player_move(row, col):
    if is_valid_move(game_board, row, col):
        game_board[row][col] = 'X'
        buttons[row][col].config(text='X', state=tk.DISABLED)
        if not update_game_state():
            computer_move()

#Intelligent

def computer_move():
    best_val = float('-inf')
    best_move = None

    for i in range(3):
        for j in range(3):
            if game_board[i][j] == '':
                game_board[i][j] = 'O'
                move_val = minimax(game_board, 0, False)
                game_board[i][j] = ''

                if move_val > best_val:
                    best_val = move_val
                    best_move = (i, j)

    if best_move:
        game_board[best_move[0]][best_move[1]] = 'O'
        buttons[best_move[0]][best_move[1]].config(text='O', state=tk.DISABLED)
        update_game_state()

#Random
"""def computer_move():
    empty_cells = [(i, j) for i in range(3) for j in range(3) if game_board[i][j] == '']
    if empty_cells:
        row, col = random.choice(empty_cells)
        game_board[row][col] = 'O'
        buttons[row][col].config(text='O', state=tk.DISABLED)
        update_game_state()"""


def minimax(board, depth, is_maximizing):
    scores = {'X': -1, 'O': 1, 'draw': 0}

    winner = check_winner(board)
    if winner:
        return scores[winner]

    if is_board_full(board):
        return scores['draw']

    if is_maximizing:
        max_eval = float('-inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == '':
                    board[i][j] = 'O'
                    eval = minimax(board, depth + 1, False)
                    board[i][j] = ''
                    max_eval = max(max_eval, eval)
        return max_eval

    else:
        min_eval = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == '':
                    board[i][j] = 'X'
                    eval = minimax(board, depth + 1, True)
                    board[i][j] = ''
                    min_eval = min(min_eval, eval)
        return min_eval

def update_game_state():
    winner = check_winner(game_board)
    if winner:
        result_label.config(text=f"{winner} wins!")
        disable_all_buttons()
        return True
    elif is_board_full(game_board):
        result_label.config(text="It's a draw!")
        disable_all_buttons()
        return True
    return False

def disable_all_buttons():
    for row in buttons:
        for button in row:
            button.config(state=tk.DISABLED)

def reset_game():
    global game_board
    game_board = [['' for _ in range(3)] for _ in range(3)]

    for i in range(3):
        for j in range(3):
            buttons[i][j].config(text='', state=tk.NORMAL)

    result_label.config(text='')

if __name__ == "__main__":
    game_board = [['' for _ in range(3)] for _ in range(3)]

    root = tk.Tk()
    root.title("Tic Tac Toe")

    buttons = [[None for _ in range(3)] for _ in range(3)]

    for i in range(3):
        for j in range(3):
            buttons[i][j] = tk.Button(root, text='', font=('Arial', 24), width=5, height=2,
                                       command=lambda row=i, col=j: player_move(row, col))
            buttons[i][j].grid(row=i, column=j)

    result_label = tk.Label(root, text='', font=('Arial', 14))
    result_label.grid(row=3, columnspan=3)

    reset_button = tk.Button(root, text='Reset Game', command=reset_game)
    reset_button.grid(row=4, columnspan=3)

    root.mainloop()
