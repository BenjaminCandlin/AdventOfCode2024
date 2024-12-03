import re

# Import data
with open(r"Day3\day3_input.txt", "r") as data:
    memory = data.read()

# Find all mul statements
list = re.findall("mul\([0-9]{1,3},[0-9]{1,3}\)", memory)

# Multiply and sum
total = 0

for item in list:
    nums = re.findall("[0-9]{1,3}", item)
    total += int(nums[0]) * int(nums[1])

print(total)

# Part Two

list2 = re.findall("mul\([0-9]{1,3},[0-9]{1,3}\)|do\(\)|don't\(\)", memory)

do_state = True

total2 = 0
for item in list2:
    if item == "do()":
        do_state = True
        continue
    if item == "don't()":
        do_state = False
        continue

    nums = re.findall("[0-9]{1,3}", item)
    if do_state is True:
        total2 += int(nums[0]) * int(nums[1])

print(total2)
