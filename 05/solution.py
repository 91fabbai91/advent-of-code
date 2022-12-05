import os
import sys
import copy
from collections import deque

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from aoc_utils import timer_func, logging_func

def parse_state(state: list):
    state_stack = []
    # get the number of stacks
    numbers = state.pop()
    numbers = list(filter(None,numbers.split(" ")))
    for number in numbers:
        state_stack.append(deque())
    # reverse to fill the stacks in the right order (last in, last out)
    state.reverse()
    #print(state)
    for row in state:
        # * as placeholder for an empty spot 
        counter = 0
        index_deque = 0
        letters = row.replace('[','').replace(']','')
        for letter in letters:
            #append letter to stack
            if letter ==' ':
                counter+=1  
                if counter == 4:
                    index_deque += 1
                    counter = 0
                    continue
            else:   
                state_stack[index_deque].append(letter)
                index_deque +=1
                counter = 0       
    return state_stack

@logging_func(filename=os.path.dirname(__file__) +'/log.log', level='DEBUG', format='%(asctime)s %(message)s')
def execute_command(state_stack: list, command: str):
    amount, start_stack, goal_stack  = command.rstrip().replace('move ','').replace(' from ',' ').replace(' to ',' ').split(' ')
    for i in range(0,int(amount)):
        letter = state_stack[int(start_stack)-1].pop()
        state_stack[int(goal_stack)-1].append(letter)
    return state_stack

@logging_func(filename=os.path.dirname(__file__) +'/log.log', level='DEBUG', format='%(asctime)s %(message)s')
def execute_command_9001(state_stack: list, command: str):
    amount, start_stack, goal_stack  = command.rstrip().replace('move ','').replace(' from ',' ').replace(' to ',' ').split(' ')
    letters = []
    for i in range(0,int(amount)):
        letters.append(state_stack[int(start_stack)-1].pop())
    # to get the behaviour to grab multiple containers at once
    letters.reverse()
    for letter in letters:
        state_stack[int(goal_stack)-1].append(letter)
    return state_stack





        




if __name__ == "__main__":
    with open(os.path.dirname(__file__) + "/input.txt",'r') as file: 
        lines = file.readlines()
        
        separating_index = lines.index("\n")
        lines = [line.rstrip() for line in lines]
        start_state = lines[0:separating_index]
        commands = lines[separating_index+1:]
        state_stacks = parse_state(start_state)
        state_stacks_task_1  = copy.deepcopy(state_stacks)
        state_stacks_task_2  = copy.deepcopy(state_stacks)
        for command in commands:
            state_stacks_task_1 = execute_command(state_stacks_task_1 , command)
            state_stacks_task_2 = execute_command_9001(state_stacks_task_2 , command)
        solution_task_1 =""
        for stack in state_stacks_task_1:
            solution_task_1 += stack.pop()
        solution_task_2 =""
        for stack in state_stacks_task_2:
            solution_task_2 += stack.pop()
        print(f"Solution Task 1: {solution_task_1}")
        print(f"Solution Task 2: {solution_task_2}")