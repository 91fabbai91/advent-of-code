import os
import sys
import math

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from aoc_utils import timer_func
from operator import add, sub, mul, floordiv, mod


class Operation():

    def __init__(self, operator_str):
        self.__number = 0
        if operator_str.startswith("+"):
            self.__operator = add
            _, number = operator_str.split(" ")
        elif operator_str.startswith("-"):
            self.__operator = sub
            _, number = operator_str.split(" ")
        elif operator_str.startswith("*"):
            self.__operator = mul
            if operator_str.endswith("old"):
                self.__operator = mul
                number = -1
            else:
                _, number = operator_str.split(" ")
        elif operator_str.startswith("/"):
            self.__operator = truediv
            _, number = operator_str.split(" ")
        else:
            raise ValueError("Wrong Operation!")
        self.__number = int(number)

    
    def do_operation(self, first_number):
        second_number = self.__number
        if self.__number<0: 
            second_number =first_number
        return self.__operator(first_number,second_number)

class Test():
    def __init__(self, divisor, recipient1_nr: int,recipient2_nr: int):
        self.__divisor = divisor
        self.__recipient1_nr=recipient1_nr
        self.__recipient2_nr=recipient2_nr
        self.__recipient1 = None
        self.__recipient2 = None

    @property
    def divisor(self):
        return self.__divisor
    @property
    def recipient1_nr(self):
        return self.__recipient1_nr

    @property
    def recipient2_nr(self):
        return self.__recipient2_nr

    @property
    def recipient1(self):
        return self.__recipient1

    @property
    def recipient2(self):
        return self.__recipient2

    @recipient1.setter
    def recipient1(self, recipient):
        self.__recipient1 = recipient

    
    @recipient2.setter
    def recipient2(self, recipient):
        self.__recipient2 = recipient

    def test_item(self, item,limiting_operation, number):
        item = limiting_operation(item,number)
        if item % self.__divisor == 0:
            self.__recipient1.add_item_with_operation(item)
        else:
            self.__recipient2.add_item_with_operation(item)
        
            
            



class Monkey():

    @property
    def test(self):
        return self.__test

    @property
    def items_inspected(self):
        return self.__items_inspected
    @property
    def id(self):
        return self.__id
    @property
    def items(self):
        return self.__items



    def reset_number_inspections(self):
        self.__items_inspected = 0
    

    
    def add_item_with_operation(self, item: int):
        self.__items.append(item)  

    
    def inspect_and_throw(self,limiting_operation, number):
        for item in self.__items:
            self.__items_inspected +=1
            item = self.__operation.do_operation(item)
            self.__test.test_item(item,limiting_operation, number)
        self.__items.clear()
    
    def __init__(self, id, starting_items: list, operation: Operation, test: Test):
        self.__id = id
        self.__items = list(starting_items)
        self.__operation = operation
        self.__test = test
        self.__items_inspected = 0 

def parse_section_to_monkey(section: list) -> Monkey:
    monkey_id = int(section[0][7])
    _ ,starting_items = section[1].split(":")
    starting_items = starting_items.split(",")
    starting_items = [int(i) for i in starting_items]
    _ ,operation_str = section[2].split(" = ")
    operation = Operation(operation_str.replace("old ",""))
    _, divisior = section[3].split("divisible by ")
    divisior = int(divisior)
    _, reciepient1 = section[4].split("monkey ")
    reciepient1 = int(reciepient1)
    _, reciepient2 = section[5].split("monkey ")
    reciepient2 = int(reciepient2)
    test = Test(divisior,reciepient1, reciepient2)
    return Monkey(monkey_id, starting_items, operation, test)


def do_task(rounds, monkeys, limiting_operation, number):

    return monkey_inspections

    



def do_task_with_import(filename: str, rounds, limiting_operator, number=-1):
    with open(os.path.dirname(__file__) + "/"+filename,'r') as file: 
        monkey_parsing = []
        monkeys = []
        lines = file.readlines()
        for line in lines:
            if line == '\n':
                monkeys.append(parse_section_to_monkey(monkey_parsing))
                monkey_parsing.clear()
            else:
                monkey_parsing.append(line.rstrip())
        monkeys.append(parse_section_to_monkey(monkey_parsing))
        product_of_primes = 1
        for monkey in monkeys:
            monkey.test.recipient1 = monkeys[monkey.test.recipient1_nr]
            monkey.test.recipient2 = monkeys[monkey.test.recipient2_nr]
            product_of_primes *= monkey.test.divisor
        if(number==-1):
            number = product_of_primes
        for i in range(rounds):
            print(f"round {i} of {rounds}", flush=True,end='\r')
            for monkey in monkeys:
                monkey.inspect_and_throw(limiting_operator, number)         
    monkey_inspections = [monkey.items_inspected for monkey in monkeys]
    print(f"Monkey Inspections {monkey_inspections}")
    monkey_inspections.sort(reverse=True)
    print(f"Solution task: {monkey_inspections[0]*monkey_inspections[1]}")

if __name__ == "__main__":
    do_task_with_import("input.txt",20,floordiv,3)
    do_task_with_import("input.txt",10000,mod,)
    