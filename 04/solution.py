import os
import sys
import random

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from aoc_utils import timer_func, logging_func

def do_list_overlap(list1: str, list2: str):
    return list(set(list1).intersection(list2)) != []

@logging_func(filename=os.path.dirname(__file__) +'/log.log', level='DEBUG', format='%(asctime)s %(message)s')
def interval_to_number_list(interval: str):
    first_number, second_number = interval.split("-")
    first_number = int(first_number)
    second_number = int(second_number)
    if first_number > second_number:
        raise ValueError(f"First interval limits needs to be smaller or equal than the second one. In this case it was {first_number} and {second_number}")
    number_list = ""
    for i in range(int(first_number), int(second_number)+1):
        number_list += str(f"{i:02}") + ","
    return number_list

@timer_func

def do_calculation_tasks(lines):
    intervals = []
    number_lists = []
    counter_a = 0
    counter_b = 0
    for line in lines:
        first_interval, second_interval = line.split(",")
        first_list = interval_to_number_list(first_interval)
        second_list = interval_to_number_list(second_interval.rstrip())
        # task 1
        if first_list in second_list or second_list in first_list:
            counter_a+=1
        first_list = list(filter(None,first_list.split(",")))
        second_list = list(filter(None,second_list.split(",")))
        #task 2
        if do_list_overlap(first_list,second_list):
            counter_b +=1
    return counter_a, counter_b

if __name__ == "__main__":
    with open(os.path.dirname(__file__) + "/input.txt",'r') as file: 
        lines = file.readlines()
        counter_a, counter_b = do_calculation_tasks(lines)
            
        print(f"Solution Task 1: {counter_a}")
        print(f"Solution Task 2: {counter_b}")
        
