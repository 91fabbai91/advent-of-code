import os
import sys
import numpy as np

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from aoc_utils import timer_func, logging_func


def find_one_letter(pattern: np.array, letter: str):
    if len(letter) != 1:
        raise ValueError(f"Length of letter was not 1. It was {len(letter)}")
    letter_count = np.count_nonzero(np.char.count(pattern,letter)==1)
    if(letter_count>1):
        raise ValueError(f"Value of H needs to be one time in pattern, but was {np.count_nonzero(pattern=='H')} times")
    elif(letter_count<1):
        return None, None
    i,j = np.where(np.char.count(pattern,letter)==1)
    return i[0], j[0]

def resize_pattern(direction: str, count: int, pattern: np.array,visited_fields: np.array):

    rows, cols = pattern.shape
    i,j = find_one_letter(pattern, "H")
    if(direction == "U"):
        #check if pattern is big enough
        missing_elements = count - i 
        if(missing_elements>0):
            pattern = np.append(np.full((missing_elements,cols),''),pattern,0)
            visited_fields = np.append(np.full((missing_elements,cols),''),visited_fields,0)
    elif(direction == "D"):
        #check if pattern is big enough
        missing_elements = i + count - (rows -1)
        if(missing_elements>0):
            pattern = np.append(pattern,np.full((missing_elements,cols),''),0)
            visited_fields = np.append(visited_fields,np.full((missing_elements,cols),''),0)
    elif(direction == "L"):
        #check if pattern is big enough
        missing_elements = count - j
        if(missing_elements>0):
            pattern = np.append(np.full((rows,missing_elements),''),pattern,1)
            visited_fields = np.append(np.full((rows,missing_elements),''),visited_fields,1)
    elif(direction == "R"):
        #check if pattern is big enough
        missing_elements = j + count - (cols -1)
        if(missing_elements>0):
            pattern = np.append(pattern, np.full((rows,missing_elements),''),1)
            visited_fields = np.append(visited_fields, np.full((rows,missing_elements),''),1)
    else:
        raise ValueError(f"No valid direction. Your direction was {direction}, but valid ones are U, D, L, R")
    return pattern, visited_fields

def move_head(direction:str, pattern: np.array, head: str, tail: str):
    x=0
    y=0
    h_y_before,h_x_before = find_one_letter(pattern,head)
    if h_y_before is None and h_x_before is None:
        return pattern,x,y
    t_y,t_x = find_one_letter(pattern,tail)
    if (t_x is None and t_y is None):
        t_x = h_x_before
        t_y = h_y_before
    diff_x_before = h_x_before - t_x
    diff_y_before = h_y_before - t_y
    if(direction == "U"):
            pattern[h_y_before-1,h_x_before] = np.char.add(pattern[h_y_before-1,h_x_before], head)
            pattern[h_y_before,h_x_before] = np.char.replace(pattern[h_y_before,h_x_before],head,"")
    elif(direction == "D"):
            pattern[h_y_before+1,h_x_before]= np.char.add(pattern[h_y_before+1,h_x_before],head)
            pattern[h_y_before,h_x_before] = np.char.replace(pattern[h_y_before,h_x_before],head,"")
    elif(direction == "L"):
            pattern[h_y_before,h_x_before-1]=np.char.add(pattern[h_y_before,h_x_before-1],head)
            pattern[h_y_before,h_x_before] = np.char.replace(pattern[h_y_before,h_x_before],head,"")
    elif(direction == "R"):
            entry_before = pattern[h_y_before,h_x_before+1]
            test = np.char.add(entry_before,head)
            pattern[h_y_before,h_x_before+1] = test
            pattern[h_y_before,h_x_before] = np.char.replace(pattern[h_y_before,h_x_before],head,"")
    else:
        raise ValueError(f"No valid direction. Your direction was {direction}, but valid ones are U, D, L, R")
    h_y_after,h_x_after = find_one_letter(pattern, head)
    diff_x_after = h_x_after - t_x
    diff_y_after = h_y_after - t_y
    if diff_y_before == 0 and diff_x_before == 0:
        pattern[t_y,t_x]= np.char.add(pattern[t_y,t_x],tail)
    elif(abs(diff_x_after)>1):
        y=0
        x = np.sign(diff_x_after)*1
        if(abs(diff_y_after)>0):
            y = np.sign(diff_y_after)*1
        pattern[t_y,t_x] = np.char.replace(pattern[t_y,t_x],tail,"")
        pattern[t_y+y,t_x+x]=np.char.add(pattern[t_y+y,t_x+x],tail)

    elif(abs(diff_y_after)>1):
        x=0
        y = np.sign(diff_y_after)*1
        if(abs(diff_y_after)>0):
            x = np.sign(diff_x_after)*1
        pattern[t_y,t_x] = np.char.replace(pattern[t_y,t_x],tail,"")
        pattern[t_y+y,t_x+x] = np.char.add(pattern[t_y+y,t_x+x],tail)
    return pattern, x,y

def move_tail(pattern: np.array, head: str, tail, x, y):
    rows, cols = pattern.shape
    h_y_after,h_x_after = find_one_letter(pattern, head)
    if h_y_after is None and h_x_after is None:
        return pattern, 0,0
    t_y,t_x = find_one_letter(pattern,tail)
    if t_y is not None and t_x is not None:
        diff_x_after = h_x_after - t_x
        diff_y_after = h_y_after - t_y

    if t_y is None and t_x is None:
        if abs(y)>0 or abs(x)>0:
            if h_y_after-y>=0 and h_x_after-x>=0 and h_y_after-y>=0 and h_x_after-x<cols and h_y_after-y<rows:
                pattern[h_y_after-y, h_x_after-x]=np.char.add(pattern[h_y_after-y, h_x_after-x],tail)
    elif(abs(diff_x_after)>1):
        y=0
        x = np.sign(diff_x_after)*1
        if(abs(diff_y_after)>0):
            y = np.sign(diff_y_after)*1
        pattern[t_y,t_x]=np.char.replace(pattern[t_y,t_x],tail,"")
        pattern[t_y+y,t_x+x] = np.char.add(pattern[t_y+y,t_x+x],tail)

    elif(abs(diff_y_after)>1):
        x=0
        y = np.sign(diff_y_after)*1
        if(abs(diff_y_after)>0):
            x = np.sign(diff_x_after)*1
        pattern[t_y,t_x] = np.char.replace(pattern[t_y,t_x],tail,"")
        pattern[t_y+y,t_x+x] = np.char.add(pattern[t_y+y,t_x+x],tail)
    else:
        x=0
        y=0
    return pattern,x, y


def fill_visited_fields(pattern: np.array, visited_fields: np.array, last_tail: str):
    t_y,t_x= find_one_letter(pattern,last_tail)
    if t_y is not None or t_x is not None:
        visited_fields[t_y,t_x] = '#'
    return visited_fields



if __name__ == "__main__":
    with open(os.path.dirname(__file__) + "/input.txt",'r') as file: 
        lines = file.readlines()
        visited_fields = np.full((1, 1), '',dtype="U1")
        pattern = np.full((1, 1), 'H',dtype="U4")
        for act_line, line in enumerate(lines):
            print(f"{act_line} of {len(lines)}")
            direction, count = line.rstrip().split(" ")
            count = int(count)
            pattern, visited_fields = resize_pattern(direction, count, pattern,visited_fields)
            while(count>0):
                pattern,x,y = move_head(direction, pattern,"H","1")
                pattern,x,y = move_tail(pattern,"1","2",x,y)
                pattern,x,y = move_tail(pattern,"2","3",x,y)
                pattern,x,y = move_tail(pattern,"3","4",x,y)
                pattern,x,y = move_tail(pattern,"4","5",x,y)
                pattern,x,y = move_tail(pattern,"5","6",x,y)
                pattern,x,y = move_tail(pattern,"6","7",x,y)
                pattern,x,y = move_tail(pattern,"7","8",x,y)
                pattern,x,y = move_tail(pattern,"8","9",x,y)
                visited_fields = fill_visited_fields(pattern, visited_fields,"9")
                count-=1
        print(f"Solution task 1: {np.count_nonzero(visited_fields=='#')}")
