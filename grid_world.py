import numpy as np
import matplotlib.pyplot as plt

def make_grid(size):
    grid = np.zeros((size,size))
    return grid

def add_wall(grid, col, gap_rows):
    for row in range(len(grid)):
        if row not in gap_rows:
            grid[row,col] =1
    return grid

def check_point(grid,point,name):
    row , col = point
    assert grid[row,col] == 0, f"{name} at {point} is inside a wall"

def plot_grid(grid, start, goal):
    plt.imshow(grid, cmap="gray_r")
    plt.scatter(start[1],start[0], color= "green",s=200)
    plt.scatter(goal[1],goal[0], color="red", s=200)
    plt.title("Grid World")
    plt.xlabel("column (x)")
    plt.ylabel("row (y)")
    plt.show()

start = (7, 2)   # (row, col)
goal = (5, 0)

grid = make_grid(10)
grid = add_wall(grid, col=2, gap_rows=[7, 8])

check_point(grid, start, "Start")
check_point(grid, goal, "Goal")

plot_grid(grid, start, goal)
