import sys
import os


def import_input(*args):
    # Import data
    if not args:
        scriptname = sys.argv[0]
        filename = scriptname.split(".")[0] + "_input.txt"
    else:
        filename = args[0]

    with open(filename, "r") as data:
        lines = data.readlines()
        output = []
        for line in lines:
            output.append(line.strip())
        return output
