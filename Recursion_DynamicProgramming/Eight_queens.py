'''
Write an algorithm to print all ways of arranging eight queens on an 8x8 chess board
so that none of them share the same row, column, or diagonal. In this case, "diagonal" means all
diagonals, not just the two that bisect the board
'''
#let the 8*8 chess board be a matrix
def eight_queen(n):
    if n==0:
        print()
