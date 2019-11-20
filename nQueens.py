# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 14:08:28 2019

@author: DERSU GIRITLIOGUL
"""

"""
N-QUEENS PROBLEM
http://claymath.org/events/news/8-queens-puzzle
"""

import numpy as np
from termcolor import colored

n = 8

def printBoard(board):
    for i in range(board.shape[0]):
        for j in range(board.shape[1]):
            if board[i][j]:
                print(colored('Q','yellow'),end=" | ")
            else:
                print("-",end=" | ")
        print("\n"+"_"*board.shape[0]*4)

def createBoard(n):
    """
    Empty slots are 0s.
    """
    return np.zeros((n,n))

def availBoard(board):
    """
    0s are the places available for new Queens.
    That is, the squares that are not threatened by any other Queens.
    """
    avail = np.copy(board)
    # Rowwise
    for i in range(board.shape[0]):
        if board[i].any():
            avail[i] = np.ones(avail[i].shape[0])

    # Columnwise
    for i in range(board.shape[1]):
        if board[:,i].any():
            avail[:,i] = np.ones(avail[:,i].shape[0])

    # Cross
    for i in range(board.shape[0]):
        for j in range(board.shape[1]):
            if board[i][j] == 1:
                savei = i
                savej = j
                while board.shape[0]>i>=0 and board.shape[1]>j>=0:
                    avail[i][j] = 1
                    i +=1
                    j +=1
                    
                i = savei
                j = savej
                while board.shape[0]>i>=0 and board.shape[1]>j>=0:
                    avail[i][j] = 1
                    i -=1
                    j +=1
                    
                i = savei
                j = savej
                while board.shape[0]>i>=0 and board.shape[1]>j>=0:
                    avail[i][j] = 1
                    i +=1
                    j -=1
                    
                i = savei
                j = savej
                while board.shape[0]>i>=0 and board.shape[1]>j>=0:
                    avail[i][j] = 1
                    i -=1
                    j -=1
                
        
    return avail

def placeQueens(board):
    for emptyrow in range(board.shape[0]):
        if not board[emptyrow].any():
            break
    
    # place a queen in the empty row
    avail = availBoard(board)
    
    
# =============================================================================
# def main():
#     board = createBoard(n)
#     placeQueens(board)
# =============================================================================
