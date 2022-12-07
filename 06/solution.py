import os
import sys

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from aoc_utils import timer_func, logging_func


@timer_func
def find_four_different_letters(line: str, marker_offset):
    for i in range(marker_offset,len(line),1):
        different_letters = set()
        different_letters.update(line[i-marker_offset:i])
        if len(different_letters) == marker_offset:
            return i

if __name__ == "__main__":
    with open(os.path.dirname(__file__) + "/input.txt",'r') as file: 
        lines = file.readlines()
        for line in lines:
            line.rstrip()
            print(find_four_different_letters(line,14))
