from dataclasses import dataclass
from pprint import pprint
from time import sleep
from typing import List

puzzle_input = open('./06/example', encoding='utf-8').read().splitlines()

# get locations of everything
x_max = len(puzzle_input) - 1
y_max = len(puzzle_input[0]) - 1
obstacles = []
guard = None

for x in range(len(puzzle_input)):
    for y in range(len(puzzle_input[0])):
        match puzzle_input[x][y]:
            case '#':
                obstacles.append((x, y))
            case '^':
                guard = (x, y)

# now move around the guard -- "play the game"
positions = set()
new_obstacles = set()
guard_moving = 90
#print(guard)
while guard[0] <= x_max and guard[1] <= y_max and guard[0] >= 0 and guard[1] >= 0:
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

    # check if we are intersecting a previous path
    if guard in positions and next_loc not in obstacles:
        new_obstacles.add(next_loc)
        print(next_loc)
    
    if next_loc in obstacles:
        guard_moving += 90
        if guard_moving == 360:
            guard_moving = 0
    else:
        positions.add(guard)
        guard = next_loc

        

print('Part 2')
print(len(new_obstacles))

    