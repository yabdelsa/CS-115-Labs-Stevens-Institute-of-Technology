#
# life.py - Game of Life lab
#
# Name: Yahia Abdelsalam
# Pledge: "I pledge my honor that I have abided by the Stevens Honor System" 
#

import random
import sys

def createOneRow(width):
    """Returns one row of zeros of width "width"...  
       You should use this in your
       createBoard(width, height) function."""
    row = []
    for col in range(width):
        row += [0]
    return row

def createBoard(width, height):
    """
    Creates a 2D grid of zeros with the given width and height
    """
    board = []
    for col in range(height):
        board.append(createOneRow(width))
        return board

def printBoard(A):
    """
    Prints the 2D array A in a visually readable way
    """
    for row in A:
        for col in row:
            sys.stdout.write(str(col)) #Prints each cell without spaces
        sys.stdout.write('\n')

def diagonalize(width, hieght):
    """
    Creates a grid with ones along the diagonal, zeros elsewhere
    """
    board = createBoard(width, height)
    for row in range(height):
        for col in range(width):
            if row == col:
                board[row][col] = 1
    return board

def innerCells(width, height):
    """
    Creates a grid with random ones and zeros in the inner cells
    """
    board = createBoard(width, height)
    for row in range(1, height - 1):
        for col in range(1, width - 1):
            board[row][col] = random.choice([0, 1])
    return board

def copy(A):
    """
    Creates a deep copy of the 2D array A
    """
    width = len(A[0])
    height = len(A)
    newBoard = createBoard(width, height)
    for row in range(width):
        newBoard[row][col] = A[row][col]
    return newBoard

def innerReverse(A):
    """
    Reverses the inner cells (1 becomes 0, 0 becomes 1)
    """
    width = len(A[0])
    height = len(A)
    newBoard = copy(A)
    for row in range(1, height - 1):
        for col in range(1, width - 1):
            newBoard[row][col] = 1 - A[row][col]
    return newBoard
                


def countNeighbors(row, col, A):
    """
    Counts the live neighbors (value 1) of a cell in the grid A.
    """
    neighbors = 0
    for dr in [-1, 0, 1]:  # Check all rows around the cell
        for dc in [-1, 0, 1]:  # Check all columns around the cell
            if dr == 0 and dc == 0:
                continue  
            r, c = row + dr, col + dc
            if 0 <= r < len(A) and 0 <= c < len(A[0]):  
                neighbors += A[r][c]
    return neighbors


def next_life_generation(A):
    """
    Generates the next board state in Conway's Game of Life.
    """
    width = len(A[0])
    height = len(A)
    newBoard = copy(A)  # Start with a deep copy
    for row in range(1, height - 1):
        for col in range(1, width - 1):
            live_neighbors = countNeighbors(row, col, A)
            if A[row][col] == 1:  # Current cell is alive
                if live_neighbors < 2 or live_neighbors > 3:
                    newBoard[row][col] = 0  # Dies from loneliness or overcrowding
            else:  # Current cell is dead
                if live_neighbors == 3:
                    newBoard[row][col] = 1  # Becomes alive from reproduction
    return newBoard










































            
