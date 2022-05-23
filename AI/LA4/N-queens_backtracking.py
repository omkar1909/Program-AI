# The N queens puzzle is the problem of placing N chess queens on an N×N chessboard so that no two queens threaten each other. 
# Thus, a solution requires that no two queens share the same row, column, or diagonal.

''' Backtracking solution - The idea is to place queens one by one in different columns, starting from the leftmost column. When we place a queen in a column, 
    we check for clashes with already placed queens. In the current column, if we find a row for which there is no clash, we mark this row and column as part 
    of the solution. If we do not find such a row due to clashes then we backtrack and return false. '''

# Python3 program to solve N Queens Problem using backtracking solution :
global N
# Here, we declare N as 4 (4 queens problem, as N=4 here)
N = 4

# function to print solution
def printSolution(board):
    for i in range(N):
        for j in range(N):
            print (board[i][j], end = " ")
        print()
 
''' A utility function to check if a queen can be placed on board[row][col]. 
    Note that this function is called when "col" queens are already placed in columns from 0 to col -1.
    So we need to check only left side for attacking queens. '''
def isSafe(board, row, col):
 
    # Check this row on left side
    for i in range(col):
        if board[row][i] == 1:
            return False
 
    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1),
                    range(col, -1, -1)):
        if board[i][j] == 1:
            return False
 
    # Check lower diagonal on left side
    for i, j in zip(range(row, N, 1),
                    range(col, -1, -1)):
        if board[i][j] == 1:
            return False
 
    return True
 
def solveNQUtil(board, col):
     
    # base case: If all queens are placed, then return true
    if col >= N:
        return True
 
    # Consider this column and try placing this queen in all rows one by one
    for i in range(N):
 
        if isSafe(board, i, col):
             
            # Place this queen in board[i][col]
            board[i][col] = 1
 
            # recur to place rest of the queens
            if solveNQUtil(board, col + 1) == True:
                return True
 
            # If placing queen in board[i][col] doesn't lead to a solution, then
            # queen from board[i][col] = 0
            board[i][col] = 0
 
    # if the queen can not be placed in any row in
    # this column col then return false
    return False
 
''' This function solves the N Queens problem using backtracking.
    It mainly uses solveNQUtil() to solve the problem. It returns false if queens
    cannot be placed, otherwise returns true and places the queens in the form of 1s.

    There may be more than one solution, but this function prints one of the feasible solutions. '''

def solveNQ():
    
    board = [ [0, 0, 0, 0],
              [0, 0, 0, 0],
              [0, 0, 0, 0],
              [0, 0, 0, 0]]
 
    if solveNQUtil(board, 0) == False:
        print ("Solution does not exist.")
        return False
 
    # print the solution
    printSolution(board)
    return True
 
# Driver Code
solveNQ()