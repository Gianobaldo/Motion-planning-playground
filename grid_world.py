import numpy as np
import matplotlib.pyplot as plt

#map
grid = np.zeros((10,10))

start = (2,7) #row and col
goal = (5,0)

''' 
#loop way
for row in range(10):
    if row != 7 and row != 8: #gap at rows7,8
        grid[row,2] = 1 #wall in column 2
        '''

#slicing
grid[0:7,2] = 1 #rows 0 - 6 , col 2 (for wall)
grid[9:10,2] = 1 #row 9, col 2 (last part of wall)

plt.imshow(grid, cmap="gray_r")
plt.scatter(start[1],start[0], color= "green",s=200)
plt.scatter(goal[1],goal[0], color="red", s=200)
plt.title("Grid World")
plt.xlabel("column (x)")
plt.ylabel("row (y)")
plt.show()