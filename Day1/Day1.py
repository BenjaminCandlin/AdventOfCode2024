# Create empty lists
left = []
right = []

# Import data
with open("Day1\input.txt", "r") as data:
    lines = data.readlines()
    for l in lines:
        split_line = l.split("   ")
        left.append(int(split_line[0]))
        right.append(int(split_line[1]))


# Sort lists
left.sort()
right.sort()


# Define difference function
def abs_difference(a, b):
    return abs(a - b)


# Find difference and sum
difference = sum(map(abs_difference, left, right))

print(difference)


# Part 2

left_multiplied = []

# Define multiply function
for i in range(len(left)):
    left_multiplied.append(left[i] * right.count(left[i]))


print(sum(left_multiplied))
