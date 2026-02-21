cols = 8
rows = 8
bw = ["■","□"]
board = [[bw[abs(row%2 - col%2)] for col in range(cols)] for row in range(rows)]
board[1] = ["♙" for col in range(cols)]
board[6] = ["♟" for col in range(cols)]
BPiece = ["♖", "♘", "♗", "♕", "♔", "♗", "♘", "♖"]
WPiece = ["♜", "♞", "♝", "♛", "♚", "♝", "♞", "♜"]
board[0] = BPiece
board[7] = WPiece
WPieceMap = {"R":"♜", "N":"♞", "B":"♝", "Q":"♛", "K":"♚"}
BPieceMap = {"R":"♖", "N":"♘", "B":"♗", "Q":"♕", "K":"♔"}

def print_board():
    for row in range(rows):
        for col in range(cols):
            rep  = board[row][col]
            print(rep,end=" ")
        print()
        
def handle_move(move):
    loc0 = move[:2]
    locF = move[2:]
    if loc0[0].isalpha() and loc0[1].isnumeric() and locF.isalpha() and locF.isnumeric() and 
    map(ord, loc0[0]) is in range(97, 105) and loc0[1] is in range(1, 9) and map(ord, locF[0]) is in range(97, 105) and locF[1] is in range(1, 9):

    else: 
        return False

        


    move = 
    rowNum = 8-x





    return


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