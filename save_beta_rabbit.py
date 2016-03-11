#!/usr/bin/python

def answer(food, grid):
    gridWidth = len(grid[0]); gridHeight = len(grid)
    curX = curY = 0; goalX, goalY = gridWidth - 1, gridHeight - 1
    steps = goalX + goalY

    while (curX & curY) != (goalX & goalY):
        if curX == goalX:  curY += 1
        elif curY == goalY:  curX += 1
        else:
            a = grid[curY][curX+1]; b = grid[curY+1][curX]
            
        food -= grid[curY][curX]
        if food < 0:  food = -1

    return food
    

print answer(12, [[0,3,5,1],[1,1,2,3],[2,4,1,2],[1,3,2,1]])
