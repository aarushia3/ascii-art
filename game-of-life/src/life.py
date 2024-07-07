import numpy as np
import random

def deadState(height: int, width: int) -> np.ndarray:
    '''
    Return a board with all zeros of the given height and width.

    Arguments: integer height, integer width
    '''
    return np.zeros((height, width), dtype = int)

def randomizeBoard(board: np.ndarray) -> np.ndarray:
    '''
    Randomize the given board and initialize it to ones and zeros.

    Arguments: A valid board represented as a NumPy array
    '''
    newBoard = np.zeros_like(board)
    randomList = [0]*1 + [1]*1
    for i in range(board.shape[0]):
        for j in range(board.shape[1]):
            newBoard[i][j] = random.choice(randomList)
    return newBoard

def renderBoard(board: np.ndarray) -> None:
    '''
    Render the given board represented as a NumPy array to the console.

    Arguments: A valid board represented as a NumPy array
    '''
    for i in range(board.shape[0]):
        for j in range(board.shape[1]):
            if board[i][j]:
                print("# ", end='')
            else:
                print("  ", end='')
        print("\n")
    return

def countLiveNeighbors(board: np.ndarray, x: int, y: int, boardRowSize: int, boardColSize: int) -> int:
    # TO DO
    return 0

def nextBoardState(board: np.ndarray) -> np.ndarray:
    '''
    Returns the next state of the board.

    Arguments: A valid board represented as a NumPy array
    '''
    newBoard = board.copy()
    boardRowSize = newBoard.shape[0]
    boardColSize = newBoard.shape[1]
    for i in range(boardRowSize):
        for j in range(boardColSize):
            liven = countLiveNeighbors(board, i, j, boardRowSize, boardColSize)
            if (liven == 0 or liven == 1):
                newBoard[i][j] = 0
            elif (liven == 2):
                continue
            elif (liven == 3):
                newBoard[i][j] = 1
            else:
                newBoard[i][j] = 0
    return newBoard


   
myDed = deadState(20,30)
newBoard = randomizeBoard(myDed)
print(newBoard)
renderBoard(newBoard)