"""
Solution to 2021 Advent of Code D1P1
"""
import sys


def crunchDepths(fileName):
    with open(fileName, "r") as depths_file:
        previous_depth = sys.maxsize
        increase_count = 0
        loop_count = 0
        for depth in (line.strip() for line in depths_file):
            loop_count += 1
            depth = int(depth)
            if depth > previous_depth:
                increase_count += 1
            previous_depth = depth
        print("Total increases: " + str(increase_count) + "\n")
        print("Total loops: " + str(loop_count))


"""
crunchDepths("input.txt")
"""
