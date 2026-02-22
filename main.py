cols = 8
rows = 8
squares = ["■","□"]
board = [[squares[abs(row%2 - col%2)] for col in range(cols)] for row in range(rows)]
board[1] = ["♙" for col in range(cols)]
board[6] = ["♟" for col in range(cols)]
BPiece = ["♖", "♘", "♗", "♕", "♔", "♗", "♘", "♖"]
WPiece = ["♜", "♞", "♝", "♛", "♚", "♝", "♞", "♜"]
board[0] = BPiece
board[7] = WPiece
WPieceMap = {"R":"♜", "N":"♞", "B":"♝", "Q":"♛", "K":"♚"}
BPieceMap = {"R":"♖", "N":"♘", "B":"♗", "Q":"♕", "K":"♔"}
isWhiteTurn = True

def print_board():
    for row in range(rows):
        for col in range(cols):
            rep  = board[row][col]
            print(rep,end=" ")
        print()

# returns 0 if move handled successfully, -1 otherwise
def handle_move(move):
    if(len(move) != 4): return -1
    if(not(move[0].isalpha() and move[1].isnumeric() and
            move[2].isalpha() and move[3].isnumeric() )):
        return -1
    square1 = move[:2]
    square2 = move[2:]
    square1Row = 8-int(square1[1])
    square1Col = int(square1[0]-'a')
    piece = board[square1Row][square1Col]

    # Work In Progress




    return

def knightMoves(row, col):return
    
#Return union of all bishop moves
def bishopMoves(row, col):return
def getNeBishopMoves(row, col):
    currRow = row+1
    currCol = col+1
    moves = []
    enemyCount = 0
    while(currRow < 8 and currCol < 8):
        if(board[currRow][currCol] in squares):
            moves.append(tuple(currRow, currCol))
        else:
            if(isWhite(board[currRow][currCol]) == isWhiteTurn):
                return moves
            else:
                if(enemyCount == 0):
                    enemyCount += 1
                    moves.append(tuple(currRow, currCol))
                else:
                    return moves
def getSwBishopMoves(row, col):return
def getNwBishopMoves(row, col):return
def getSeBishopMoves(row, col):return

    
def rookMoves(row, col):return
def queenMoves(row, col):return (bishopMoves(row,col) + rookMoves(row,col))

def isWhite(piece):return


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