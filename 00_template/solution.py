import os
import sys

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from aoc_utils import timer_func, logging_func

if __name__ == "__main__":
    with open(os.path.dirname(__file__) + "/input.txt",'r') as file: 
        lines = file.readlines()