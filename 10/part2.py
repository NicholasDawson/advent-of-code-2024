from pprint import pprint


map = [[int(y) for y in x] for x in open('./10/input', encoding='utf-8').read().splitlines()]
x_max = len(map)
y_max = len(map[0])

def trail_score(x, y) -> list:
    height = map[x][y]

    # base case
    if height == 9:
        #print('TOP')
        return [(x, y)]
    
    # look for the next segment of a trail
    # recursive case
    nines = []
    # DOWN
    if x+1 < x_max and map[x+1][y] == height + 1:
        #print('found')
        nines += trail_score(x+1, y)
    
    # UP
    if x-1 >= 0 and map[x-1][y] == height + 1:
        #print('found')
        nines += trail_score(x-1, y)
    
    # LEFT
    if y-1 >= 0 and map[x][y-1] == height + 1:
        #print('found')
        nines += trail_score(x, y-1)

    # RIGHT
    if y+1 < y_max and map[x][y+1] == height + 1:
        #print('found')
        nines += trail_score(x, y+1)

    return nines
    
trailhead_scores = []
#pprint(map)
for i in range(len(map)):
    for j in range(len(map[0])):
        if map[i][j] == 0:
            heads = trail_score(i, j)
            pprint(heads)
            trailhead_scores.append(len(heads))

#print(trailhead_scores)
print('Part 2')
print(sum(trailhead_scores))