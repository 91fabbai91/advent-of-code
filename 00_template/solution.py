import os
import sys

sys.path.append('..')

from aoc_utils import timer_func, logging_func

if __name__ == "__main__":
    with open(os.path.dirname(__file__) + "/input.txt",'r') as file: 
        lines = file.readlines()