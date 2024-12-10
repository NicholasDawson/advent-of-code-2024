from pprint import pprint


map = [[int(y) for y in x] for x in open('./10/example', encoding='utf-8').read().splitlines()]
x_max = len(map)
y_max = len(map[0])

def trail_score(x, y) -> int:
    height = map[x][y]

    # base case
    if height == 9:
        print('TOP', x, y)
        return 1
    
    # look for the next segment of a trail
    # recursive case
    score = 0
    # DOWN
    if x+1 < x_max and map[x+1][y] == height + 1:
        #print('found')
        score += trail_score(x+1, y)
    
    # UP
    if x-1 >= 0 and map[x-1][y] == height + 1:
        #print('found')
        score += trail_score(x-1, y)
    
    # LEFT
    if y-1 >= 0 and map[x][y-1] == height + 1:
        #print('found')
        score += trail_score(x, y-1)

    # RIGHT
    if y+1 < y_max and map[x][y+1] == height + 1:
        #print('found')
        score += trail_score(x, y+1)

    return score
    
total = 0
trailhead_scores = []
pprint(map)
for i in range(len(map)):
    for j in range(len(map[0])):
        if map[i][j] == 0:
            trailhead_scores.append(trail_score(i, j))

print(trailhead_scores)
print('Part 1')
print(total)