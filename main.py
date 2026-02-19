cols = 8
rows = 8
bw = ["■","□"]
board = [[bw[abs(row%2 - col%2)] for col in range(cols)] for row in range(rows)]
board[1] = ["♙" for col in range(cols)]
board[6] = ["♟" for col in range(cols)]


def print_board():
    for row in range(rows):
        for col in range(cols):
            rep  = board[row][col]
            print(rep,end=" ")
        print()

print_board()
# def main_game_loop():return
# def initalize_state():return
# def check_win_condition():return
# def print_board():return
# def handle_move(move):return

# While the main game loop is going on
# Every iteration should end with printing the board
# Constant Data: board dimensions, piece moves, 
# We'll keep track of: board, turn, winOrNot, castling allowed, material