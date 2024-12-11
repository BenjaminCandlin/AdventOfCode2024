import sys
import os
import time
import copy

sys.path.append(r"C:\Users\BENCAND\Repos\AdventOfCode2024\AdventOfCode2024")
from custom import import_input


orig_input = import_input()
input = copy.deepcopy(orig_input)

test_input = [
    "190: 10 19",
    "3267: 81 40 27",
    "83: 17 5",
    "156: 15 6",
    "7290: 6 8 6 15",
    "161011: 16 10 13",
    "192: 17 8 14",
    "21037: 9 7 18 13",
    "292: 11 6 16 20",
]


# Function that creates list of all numbers and operations combinations for input list
def combination_creation(list):
    combinations = [[list[0]]]
    for number in list[1:]:
        temp_combinations = []
        for combination in combinations:
            combination_plus = combination + ["+"] + [number]
            combination_multiply = combination + ["*"] + [number]
            temp_combinations.append(combination_plus)
            temp_combinations.append(combination_multiply)
        combinations = copy.deepcopy(temp_combinations)
    return combinations


def calculate_combination(combination):
    for i in range(len(combination)):
        item = combination[i]
        if type(item) is str:
            continue
        if type(item) is int:
            if i == 0:
                result = item
            elif combination[i - 1] == "*":
                result *= item
            elif combination[i - 1] == "+":
                result += item
    return result


# For each line in the input work out if a combination of * and + can make the left number
def evaluate_valid(input):

    valid = []

    for line in input:
        aim = int(line.split(":")[0])
        numbers_str = line.split(":")[1].strip().split(" ")
        numbers = []
        for number in numbers_str:
            numbers.append(int(number))

        combinations = combination_creation(numbers)
        # Check all combinations
        for combination in combinations:
            if calculate_combination(combination) == aim:
                valid.append(aim)
                break

    sum_valid = sum(valid)
    return sum_valid


assert evaluate_valid(["292: 11 6 16 20"]) == 292
assert evaluate_valid(test_input) == 3749

print(evaluate_valid(input))