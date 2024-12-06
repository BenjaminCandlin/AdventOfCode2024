import sys
import os
import time
import copy

sys.path.append(r"C:\Users\BENCAND\Repos\AdventOfCode2024\AdventOfCode2024")
from custom import import_input


orig_map = import_input()
map = copy.deepcopy(orig_map)


def move_guard(guard_loc, map, obstacle):
    if guard_loc[2] == 1:
        new_guard_loc = [guard_loc[0] - 1, guard_loc[1], guard_loc[2]]
    elif guard_loc[2] == 2:
        new_guard_loc = [guard_loc[0], guard_loc[1] + 1, guard_loc[2]]
    elif guard_loc[2] == 3:
        new_guard_loc = [guard_loc[0] + 1, guard_loc[1], guard_loc[2]]
    elif guard_loc[2] == 4:
        new_guard_loc = [guard_loc[0], guard_loc[1] - 1, guard_loc[2]]
    else:
        raise ValueError("guard_loc[2] is invalid")

    # Check new location for obstacle
    if (new_guard_loc[0], new_guard_loc[1]) in obstacle:
        new_guard_loc = guard_loc
        if new_guard_loc[2] < 4:
            new_guard_loc[2] = guard_loc[2] + 1
        else:
            new_guard_loc[2] = 1

    # Replace path with "X"
    new_line = [map[guard_loc[0]][: guard_loc[1]] + "X" + map[guard_loc[0]][guard_loc[1] + 1 :]]
    new_map = map[: guard_loc[0]] + new_line + map[guard_loc[0] + 1 :]
    return new_guard_loc, new_map


# Check if still on map
def check_location(guard_loc, map):
    if guard_loc[0] > (len(map) - 1) or guard_loc[0] < 0:
        return False
    if guard_loc[1] > (len(map[0]) - 1) or guard_loc[1] < 0:
        return False
    else:
        return True


# Find guard location ("^")
for line in map:
    try:
        orig_guard_loc = [map.index(line), line.index("^"), 1]
    except ValueError:
        continue

# Find obstacle locations ("#")
obstacle = []
for i in range(len(map)):
    for j in range(len(map[i])):
        if map[i][j] == "#":
            obstacle.append((i, j))


# Store original guard position and route
guard_loc = orig_guard_loc.copy()
route = []

# Simulate movement
while check_location(guard_loc, map):
    print(guard_loc)
    guard_loc, map = move_guard(guard_loc, map, obstacle)
    route.append(guard_loc[:])

with open(r"Day6\final_map.txt", "w") as file:
    for line in map:
        file.write(line + "\n")

print("simulation complete")

print(sum(line.count("X") for line in map))


# Part 2

# Iterate for each possible new obstruction location

# Simulate test movement
test_map = import_input("Day6/test_map.txt")
test_obstacle = []
test_route = []
for line in test_map:
    try:
        test_orig_guard_loc = [test_map.index(line), line.index("^"), 1]
    except ValueError:
        continue
for i in range(len(test_map)):
    for j in range(len(test_map[i])):
        if test_map[i][j] == "#":
            test_obstacle.append((i, j))
test_guard_loc = test_orig_guard_loc.copy()
while check_location(test_guard_loc, test_map):
    test_guard_loc, test_map = move_guard(test_guard_loc, test_map, test_obstacle)
    test_route.append(test_guard_loc)


def infinite_loop_calculate(route, map, obstacle, orig_guard_loc):
    locations = []
    for location in route:
        if check_location(location, map) is False:
            break
        i, j = location[0], location[1]
        if (i, j) not in obstacle:
            obstacle.append((i, j))
            print("\nChecking", i, j)
            # Run simulation
            # Reset guard location and map
            loop_map = copy.deepcopy(map)
            if route.index(location) < 1:
                guard_loc = orig_guard_loc[:]
                print("starting at og", guard_loc)
            else:
                guard_loc = route[route.index(location) - 1][:]
                print("starting at prev", guard_loc)

            guard_loc_hist = []
            while check_location(guard_loc, loop_map):
                # Check if the guard passes the same location twice in the same direction
                if guard_loc in guard_loc_hist:
                    print("same location/direction!")
                    locations.append((i, j))
                    break
                guard_loc_hist.append(guard_loc[:])
                guard_loc, map = move_guard(guard_loc, map, obstacle)

            obstacle.remove((i, j))
    return locations


# locations = infinite_loop_calculate(test_route, test_map, test_obstacle, test_orig_guard_loc)

locations = infinite_loop_calculate(route, orig_map, obstacle, orig_guard_loc)

locations = list(set(locations))

print(locations)
print(len(locations))
