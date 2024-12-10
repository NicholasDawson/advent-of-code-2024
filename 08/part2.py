from dataclasses import dataclass
from pprint import pprint
from time import sleep
from typing import List
from itertools import combinations

puzzle_input = open('./08/input', encoding='utf-8').read().splitlines()

antennas = {}
antinodes = set()

x_max = len(puzzle_input) - 1
y_max = len(puzzle_input[0]) - 1

# read in antennas
for x in range(len(puzzle_input)):
    for y in range(len(puzzle_input[0])):
        char = puzzle_input[x][y]
        if char != '.':
            if char in antennas:
                antennas[char].append((x, y))
            else:
                antennas[char] = [(x, y)]

# iterate over antenna groups
for key in antennas:
    print(key)
    for combo in combinations(antennas[key], 2):
        first, second = combo
        print(first, second)

        # add antennas as antinodes
        antinodes.add(first)
        antinodes.add(second)

        diff = (first[0]-second[0], first[1]-second[1])
        
        anti1 = (first[0]+diff[0], first[1]+diff[1])
        while not (anti1[0] < 0 or anti1[0] > x_max or anti1[1] < 0 or anti1[1] > y_max):
            antinodes.add(anti1)
            anti1 = (anti1[0]+diff[0], anti1[1]+diff[1])
        
        anti2 = (second[0]-diff[0], second[1]-diff[1])
        while not (anti2[0] < 0 or anti2[0] > x_max or anti2[1] < 0 or anti2[1] > y_max):
            antinodes.add(anti2)
            anti2 = (anti2[0]-diff[0], anti2[1]-diff[1])

print('Part 2')
print(len(antinodes))

# create grid
visual = [['.' for x in range(y_max+1)] for x in range(x_max+1)]

# show antennas
for key in antennas:
    for a in antennas[key]:
        visual[a[0]][a[1]] = key

# show antinodes
for a in antinodes:
    visual[a[0]][a[1]] = '#'

# print grid
for x in visual:
    for y in x:
        print(y, end='')
    print()