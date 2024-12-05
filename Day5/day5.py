import sys
import os

sys.path.append(r"C:\Users\BENCAND\Repos\AdventOfCode2024\AdventOfCode2024")
from import_input import import_input


ordering_rules = import_input("Day5/ordering_rules.txt")
update_list = import_input("Day5/update_list.txt")
test_rules = import_input("Day5/test_rules.txt")

# Put ordering rules into dictionary


def convert_to_dict(ordering_rules):
    ordering_dict = {}
    for line in ordering_rules:
        key, number = line.split("|")
        key = int(key)
        number = int(number)
        if key not in ordering_dict.keys():
            ordering_dict[key] = [number]
        else:
            ordering_dict[key].append(number)
    return ordering_dict


def check_valid(update, ordering_dict=convert_to_dict(ordering_rules)):
    checked_values = []
    for value in update:
        checked_values.append(value)
        invalid_numbers = ordering_dict[value]
        for number in invalid_numbers:
            if number in checked_values:
                return False

    return True


def get_middle(list):
    middle_index = int((len(list) - 1) / 2)
    return list[middle_index]


ordering_dict = convert_to_dict(ordering_rules)
test_dict = convert_to_dict(test_rules)


assert check_valid([75, 47, 61, 53, 29], test_dict) == True
assert check_valid([75, 97, 47, 61, 53], test_dict) == False


valid_updates = []
invalid_updates = []

for line in update_list:
    int_line = list(map(int, line.split(",")))
    if check_valid(int_line) is True:
        valid_updates.append(int_line)
    else:
        invalid_updates.append(int_line)


middle_numbers = []
for list in valid_updates:
    middle_numbers.append(get_middle(list))

print(sum(middle_numbers))


# Part 2


def check_position(value, update, ordering_dict=convert_to_dict(ordering_rules)):
    invalid_numbers = ordering_dict[value]
    check_index = update.index(value)
    for number in update[:check_index]:
        if number in invalid_numbers:
            return False
    return True


# Sort invalid updates to be valid


def sort_invalid(update, ordering_dict=convert_to_dict(ordering_rules)):
    for value in reversed(update):
        while check_position(value, update, ordering_dict) is False:
            index = update.index(value)
            update.insert(index - 1, update.pop(index))
    return update


for update in invalid_updates:
    while check_valid(update) is False:
        sort_invalid(update)


invalid_middle_numbers = []
for list in invalid_updates:
    invalid_middle_numbers.append(get_middle(list))

print(sum(invalid_middle_numbers))
