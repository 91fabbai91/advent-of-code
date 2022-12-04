import os
import sys
import enum

sys.path.append('..')

from aoc_utils import timer_func

class Result(enum.IntEnum):
    WIN = 6
    DRAW = 3
    LOSE = 0

class OpStrategy(enum.IntEnum):
    A = 1
    B = 2
    C = 3

class OwnStrategy(enum.IntEnum):
    X = 1
    Y = 2
    Z = 3

class DesiredResult(enum.Enum):
    X = Result.LOSE
    Y = Result.DRAW
    Z = Result.WIN


def fight(op_strategy: OpStrategy, own_strategy: OwnStrategy):
    if own_strategy - op_strategy % 3 == 1:
        return Result.WIN,  own_strategy
    elif own_strategy - op_strategy == 0:
        return Result.DRAW, own_strategy
    else:
        return Result.LOSE, own_strategy

def fight_new_rules(op_strategy: OpStrategy, desired_result: DesiredResult):
    if desired_result == DesiredResult.Z:
        own_strategy = OwnStrategy((op_strategy.value)%3+1)
    elif desired_result == DesiredResult.Y:
        own_strategy = OwnStrategy(op_strategy.value)
    else:
        own_strategy = OwnStrategy((op_strategy.value+1)%3+1)
    return desired_result.value, own_strategy
        

@timer_func
def calculate_strategy_points(input_text_file: str):
    results = []
    total_points = 0
    total_points_2 = 0
    with open(input_text_file,'r') as file:
        lines = file.readlines()
        for line in lines:
            result, strategy = fight(OpStrategy[line[0]],OwnStrategy[line[2]])
            desired_result, strategy_2 = fight_new_rules(OpStrategy[line[0]], DesiredResult[line[2]])
            total_points = total_points + result + strategy
            total_points_2 = total_points_2 + desired_result + strategy_2
            results.append(result)
        print(f"Total points a: {total_points}")
        print(f"Total points b: {total_points_2}")


if __name__ == '__main__':
    calculate_strategy_points(os.path.dirname(__file__) + "/input.txt")