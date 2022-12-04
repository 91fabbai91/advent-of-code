import os
import sys

sys.path.append('..')

from aoc_utils import timer_func, logging_func


LOWER_ASCII_OFFSET = 97
UPPER_ASCII_OFFSET = 65
TASK_OFFSET = 27


@logging_func(filename=os.path.dirname(__file__) +'/log.log', level='DEBUG', format='%(asctime)s %(message)s')
def get_doubled_item(line1: str, line2: str):
    return list(set.intersection(set(line1), set(line2)))[0]

@logging_func(filename=os.path.dirname(__file__) +'/log.log', level='DEBUG', format='%(asctime)s %(message)s')
def get_common_item(line1: str, line2: str, line3: str):
    sets = [set(line1), set(line2), set(line3)]
    return list(set.intersection(*sets))[0]

def get_value_for_letter(letter: str):
    if len(letter) > 1:
        raise ValueError(("The Argument has to be one single letter"))
    if letter.islower():
        return ord(letter) - LOWER_ASCII_OFFSET + 1
    if letter.isupper():
        return ord(letter) - UPPER_ASCII_OFFSET + TASK_OFFSET

@timer_func
def calculate_sum_of_priorities_per_line(lines):
    sum_of_priorities = 0
    for line in lines:
        first_part, second_part = line[:len(line)//2], line[len(line)//2:]
        second_part = second_part.rstrip()
        double_item = get_doubled_item(first_part, second_part)
        priority = get_value_for_letter(double_item)
        sum_of_priorities = sum_of_priorities + priority
    return sum_of_priorities

@timer_func
def calculate_sum_of_priorities_of_three_lines(lines):
    sum_of_priorities = 0
    if len(lines) % 3 > 0:
        raise ValueError("You have to compare three lines")
    for i in range(0,len(lines), 3):
        double_item = get_common_item(lines[i].rstrip(),lines[i+1].rstrip(), lines[i+2].rstrip())

        priority = get_value_for_letter(double_item)
        sum_of_priorities = sum_of_priorities + priority
    return sum_of_priorities

def read_input_text(input_text_file: str):
    with open(input_text_file,'r') as file: 
        lines = file.readlines()
        sum_of_priorities_a = calculate_sum_of_priorities_per_line(lines)
        sum_of_priorities_b = calculate_sum_of_priorities_of_three_lines(lines)
        return sum_of_priorities_a, sum_of_priorities_b




if __name__ == "__main__":
    solution1, solution2 = read_input_text(os.path.dirname(__file__) + "/input.txt")
    print(f"Solution for part 1: {solution1}")
    print(f"Solution for part 2: {solution2}")
