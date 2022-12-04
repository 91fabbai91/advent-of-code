import os
import time
import math
import sys

sys.path.append('..')

from aoc_utils import timer_func, logging_func


@logging_func(filename=os.path.dirname(__file__) +'/log.log', level='DEBUG', format='%(asctime)s %(message)s')
def calculate_max_sum_of_calories(input_file_name: str):
    with open(input_file_name,'r') as file1:
        lines = file1.readlines()

        sum_of_calories = []
        sum = 0
        for line in lines:
            if line == '\n':
                sum_of_calories.append(sum)
                sum = 0
                continue
            sum += int(line)
    sum_of_calories.sort(reverse=True)
    return sum_of_calories

        

if __name__ == '__main__':
    sum_of_calories =calculate_max_sum_of_calories(os.path.dirname(__file__) + "/input.txt")
    print(f"Solution for first part: {sum_of_calories[0]}")
    print(f"Solution for second part: {int(math.fsum(sum_of_calories[0:3]))}")