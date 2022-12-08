import os
import sys
import numpy as np
import copy

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from aoc_utils import timer_func, logging_func

# set the outer trees as visible
def create_visibility_wood(wood: np.array):
    visibility_wood = np.zeros_like(wood)
    visibility_wood[0,:] = np.ones_like(visibility_wood[0,:])
    visibility_wood[-1,:] = np.ones_like(visibility_wood[-1,:])
    visibility_wood[:,0] = np.ones_like(visibility_wood[:,0])
    visibility_wood[:,-1] = np.ones_like(visibility_wood[:,-1])
    return visibility_wood

# search backward and forward in vertical direction
def search_vertically(wood: np.array):
    scenic_score = np.ones_like(wood)
    local_visibility_wood = np.zeros_like(wood)
    rows, cols = wood.shape
    for i in range(0,rows-1,1):
        for j in range(0,cols,1):
            offset=1
            while True:
                if wood[i,j]-wood[i+offset,j] <= 0:
                    break
                if i+offset==rows-1:
                    local_visibility_wood[i][j] = local_visibility_wood[i][j] or 1
                    break

                offset+=1
            scenic_score[i][j] = scenic_score[i][j]*abs(offset)
    for i in range(1,rows,1):
        for j in range(0,cols,1):
            offset=-1
            while True:
                if wood[i,j]-wood[i+offset,j] <= 0:
                    break
                if i+offset==0:
                    local_visibility_wood[i][j] = local_visibility_wood[i][j] or 1
                    break
                offset-=1
            scenic_score[i][j] = scenic_score[i][j]*abs(offset)
    return local_visibility_wood, scenic_score

# search horizontally in backward and forward
def search_horizontally(wood: np.array):
    local_visibility_wood = np.zeros_like(wood)
    scenic_score = np.ones_like(wood)
    rows, cols = wood.shape
    
    for i in range(0,rows,1):
        for j in range(0,cols-1,1):
            offset=1
            while True:
                if wood[i,j]-wood[i,j+offset] <= 0:
                    break
                if j+offset==cols-1:
                    local_visibility_wood[i][j] = local_visibility_wood[i][j] or 1
                    break
                offset+=1
            scenic_score[i][j] = scenic_score[i][j]*abs(offset)
    for i in range(0,rows,1):
        for j in range(1,cols,1):
            offset=-1
            while True:
                if  wood[i,j]-wood[i,j+offset] <= 0:
                    break
                if j+offset==0:
                    local_visibility_wood[i][j] = local_visibility_wood[i][j] or 1
                    break

                offset-=1
            scenic_score[i][j] = scenic_score[i][j]*abs(offset)
    return local_visibility_wood, scenic_score

if __name__ == "__main__":
    with open(os.path.dirname(__file__) + "/input.txt",'r') as file: 
        lines = file.readlines()
        total_visible_trees = 0
        wood = []
        for line in lines:
            line = line.rstrip()
            row_list = []
            for letter in line:
                row_list.append(int(letter))
            wood.append(row_list)

        wood = np.array(wood)
        visibility_wood = create_visibility_wood(wood)
        vertical_visibility, vertical_scenic_score = search_vertically(wood)
        horizontal_visibility, horizontal_scenic_score = search_horizontally(wood)
        scenic_score = np.multiply(vertical_scenic_score,horizontal_scenic_score)
        visibility_wood = np.logical_or(visibility_wood,horizontal_visibility)
        visibility_wood = np.logical_or(visibility_wood,vertical_visibility)
        print(f"Visible Trees (Task 1): {np.count_nonzero(visibility_wood==True)}")
        print(f"Maximum Scenic Score (Task 2): {scenic_score.max()}")

