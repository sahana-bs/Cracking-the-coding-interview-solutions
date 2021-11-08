'''
Robot in a Grid: Imagine a robot sitting on the upper left corner of grid with r rows and c columns.
The robot can only move in two directions, right and down, but certain cells are "off limits" such that
the robot cannot step on them. Design an algorithm to find a path for the robot from the top left to
the bottom right.
'''

#these solutions are without considering the "off limits"
def robot(r,c):     #number of rows and cols
    if r==1 or c==1:
        return 1
    return robot(r-1,c)+robot(r,c-1)

print(robot(3,3))

import numpy as np
memo=list(list())
def robot_dp(r,c):
    for i in range(r):     #the first column of all rows reachable
        memo.append([1])
    for i in range(1,r):
        for j in range(c-1):
            memo[i].append(0)

    for i in range(c-1):    #the entire first row is reachable
        memo[0].append(1)
    print(memo)           #initial setting
    for i in range(1,r):
        for j in range(1,c):
            memo[i][j]=memo[i-1][j]+memo[i][j-1]
    print(memo)
    return memo[r-1][c-1]

print(robot_dp(3,3))

'''
6   #recursive soulution

#dp solution
[[1, 1, 1], [1, 0, 0], [1, 0, 0]]
[[1, 1, 1], [1, 2, 3], [1, 3, 6]]   #each number represents the different ways in which that position can be reached.
6
'''
