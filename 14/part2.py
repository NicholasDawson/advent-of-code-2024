"""
To determine the safest area, count the number of robots in each quadrant after 100 seconds.
Robots that are exactly in the middle (horizontally or vertically) don't count as being in any quadrant,
so the only relevant robots are:

In this example, the quadrants contain 1, 3, 4, and 1 robot.
Multiplying these together gives a total safety factor of 12.

Predict the motion of the robots in your list within a space which is 101 tiles wide and 103 tiles tall.
What will the safety factor be after exactly 100 seconds have elapsed?
"""

from time import sleep
from typing import List
from collections import Counter


puzzle_input = open('./14/input', encoding='utf-8').read().splitlines()

MAX_WIDTH = 101
MAX_HEIGHT = 103

class Robot:
    def __init__(self, px, py, vx, vy):
        self.px = px
        self.py = py
        self.vx = vx
        self.vy = vy

    def move(self):
        # Move velocity
        self.px += self.vx
        self.py += self.vy

        # Wrap around
        self.px = self.px % MAX_WIDTH
        self.py = self.py % MAX_HEIGHT

    def __repr__(self):
        return f'Robot(x={self.px} y={self.py} vx={self.vx} vy={self.vy})'
    
def print_robots(robots: List[Robot]):
    grid = []
    for _ in range(MAX_HEIGHT):
        row = []
        for _ in range(MAX_WIDTH):
            row.append(' ')
        grid.append(row)
    for r in robots:
        grid[r.py][r.px] = '#'

    for y in grid:
        for x in y:
            print(x, end='')
        print()


# READ IN ROBOTS
robots: List[Robot] = []
for robot in puzzle_input:
    veq_pos = robot.find('v=')
    velocity = robot[veq_pos+2:].split(',')
    position = robot[2:veq_pos-1].split(',')
    robots.append(
        Robot(
            int(position[0]),
            int(position[1]),
            int(velocity[0]),
            int(velocity[1])
            )
        )

# PROCESS 100 seconds
for s in range(15000):
    # rows = [[] for _ in range(MAX_HEIGHT)]
    for r in robots:
        r.move()
        # rows[r.py].append(r.px)
    # alert = False
    # for r in rows:
    #     r_sorted = sorted(r)
    #     max_diff = -1
    #     for i in range(len(r_sorted)-1):
    #         diff = r_sorted[i+1] - r_sorted[i]
    #         if diff > max_diff:
    #             max_diff = diff
    #     if max_diff == 1 and len(r_sorted) > 5:
    #         alert = True
    #         break
    # if alert:
    print('SECONDS:', s)
    print_robots(robots)

# NOW COMPUTE ROBOTS PER QUADRANT
q1, q2, q3, q4 = 0, 0, 0, 0
HALF_WIDTH = MAX_WIDTH // 2
HALF_HEIGHT = MAX_HEIGHT // 2
for r in robots:
    if r.px < HALF_WIDTH and r.py < HALF_HEIGHT:
        q1 += 1
    elif r.px > HALF_WIDTH and r.py < HALF_HEIGHT:
        q2 += 1
    elif r.px < HALF_WIDTH and r.py > HALF_HEIGHT:
        q3 += 1
    elif r.px > HALF_WIDTH and r.py > HALF_HEIGHT:
        q4 += 1




