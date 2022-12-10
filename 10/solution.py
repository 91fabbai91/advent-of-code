import os
import sys
import math
import numpy as np

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from aoc_utils import timer_func, logging_func

def execute_line(line:str, register: list, cycle:int):
    if line.startswith("noop"):
        register.append(register[cycle])
        cycle+=1
    elif line.startswith("addx"):
        _, number = line.split(" ")
        register.append(register[cycle])
        register.append(register[cycle]+int(number))
        cycle+=2
    return register, cycle

def calculate_sum_of_signal_strengths(register: list, cycles_to_sum:list):
    signal_strengths = {}
    for i in cycles_to_sum:
        signal_strengths.update({i: register[i-1]*i})
    return signal_strengths

def render_image(image:np.array, register:list,cycle:int):
    rows, cols = image.shape

    col_register = register[cycle] % cols
    row_cycle = math.floor((cycle-1)/cols)
    col_cycle = (cycle) % cols
    interval_start = col_register-1
    interval_end = col_register+2
    if interval_start<0:
        interval_start = 0
    elif interval_end>39:
        interval_end=39

    interval = [i for i in range(interval_start,interval_end,1)]

    image[row_cycle, col_cycle] = "#" if col_cycle in interval else "."
    return image


if __name__ == "__main__":
    filename = "test_input.txt"
    with open(os.path.dirname(__file__) + "/"+filename,'r') as file: 
        lines = file.readlines()
        register = [1]
        cycle = 0
        cycles_to_sum_up = [20,60,100,140,180,220]
        image = np.full((6,40),".")
        for line in lines:
            register, cycle = execute_line(line.rstrip(),register,cycle)
        signal_strengths = calculate_sum_of_signal_strengths(register, cycles_to_sum_up)
        print(f"Solution task 1: {sum(signal_strengths.values())}")
        for i in range(1,len(register)):
            image = render_image(image,register,i)
        # for solution of task 2 look into the files
        with open(os.path.dirname(__file__) + "/image_"+filename,'w') as file_out:
            file_out.write(np.array2string(image,1000,separator="").replace("'","").replace("[","").replace("]",""))