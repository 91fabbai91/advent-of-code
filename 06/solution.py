import os
import sys

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from aoc_utils import timer_func, logging_func
#for task 1 MARKER_OFFSET=4 for task 2 MARKER_OFFSET = 14_
MARKER_OFFSET = 4

@timer_func
def find_four_different_letters(line: str):
    for i in range(MARKER_OFFSET,len(line),1):
        different_letters = set()
        different_letters.update(line[i-MARKER_OFFSET:i])
        if len(different_letters) == MARKER_OFFSET:
            return i

if __name__ == "__main__":
    with open(os.path.dirname(__file__) + "/input.txt",'r') as file: 
        lines = file.readlines()
        for line in lines:
            line.rstrip()
            print(find_four_different_letters(line))
