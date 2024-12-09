from dataclasses import dataclass
from pprint import pprint
from time import sleep
from typing import List

puzzle_input = open('./06/input', encoding='utf-8').read().splitlines()

# get locations of everything
x_max = len(puzzle_input) - 1
y_max = len(puzzle_input[0]) - 1
original_obstacles = []
start = None

for x in range(len(puzzle_input)):
    for y in range(len(puzzle_input[0])):
        match puzzle_input[x][y]:
            case '#':
                original_obstacles.append((x, y))
            case '^':
                start = (x, y)

def is_loop(obstacles):
    # now move around the guard -- "play the game"
    positions = set()
    guard_moving = 90
    guard = start
    repeats = 0
    while guard[0] <= x_max and guard[1] <= y_max and guard[0] >= 0 and guard[1] >= 0:
        positions.add(guard)
        next_loc = None
        match guard_moving:
            case 90:
                next_loc = (guard[0] - 1, guard[1])
            case 180:
                next_loc = (guard[0], guard[1] + 1)
            case 270:
                next_loc = (guard[0] + 1, guard[1])
            case 0:
                next_loc = (guard[0], guard[1] - 1)
        
        if next_loc in obstacles:
            guard_moving += 90
            if guard_moving == 360:
                guard_moving = 0
        else:
            guard = next_loc

        if guard in positions:
            repeats += 1
            if repeats > 10000:
                return True
        else:
            repeats = 0
    return False

loops = 0
for x in range(len(puzzle_input)):
    print(x, len(puzzle_input))
    for y in range(len(puzzle_input[0])):
        if (x, y) not in original_obstacles:
            if is_loop([(x, y)] + original_obstacles):
                loops += 1

print(loops)







    