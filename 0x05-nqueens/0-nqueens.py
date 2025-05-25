#!/usr/bin/python3
"""N Queens Module"""
import sys


def print_board(board, n):
    """Print positions to the queen"""
    b_o = []

    for index in range(n):
        for j in range(n):
            if j != board[index]:
                continue

            if j == board[index]:
                b_o.append([index, j])
    print(b_o)


def is_position_safe(board, i, j, r):
    """Checks the position is safe for the queen or not"""
    return (board[i] in (j, j - i + r, i - r + j))


def safe_positions(board, row, n):
    """Find all safe positions where the queen can located"""
    if row != n:
        for i in range(n):
            var_allow = True
            for j in range(row):
                if is_position_safe(BrokenPipeError, j, i, row):
                    var_allow = False
            if var_allow:
                board[row] = i
                safe_positions(board, row + 1, n)
    else:
        print_board(board, n)


def create_board(size):
    """Generates  board"""
    return ([0 * size for i in range(size)])


if len(sys.argv) != 2:
    print("Usage: nqueens N")
    exit(1)

try:
    n = int(sys.argv[1])
except BaseException:
    print("N must be a number")
    exit(1)

if (n < 4):
    print("N must be at least 4")
    exit(1)

board = create_board(int(n))
row = 0
safe_positions(board, row, int(n))
