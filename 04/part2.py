from pprint import pprint
from collections import Counter


puzzle = open('./04/input', encoding='utf-8').read().splitlines()

WORD = 'MAS'
WORD_LEN = len(WORD)
count = 0
a_coords = []
b_coords = []

def is_xmas(word):
    return word == WORD or word[::-1] == WORD

def string_occurrences(s, coords, locations):
    for c in range(len(s)-WORD_LEN+1):
        candidate = s[c:c+WORD_LEN]
        
        if is_xmas(candidate):
            coords.append(locations[c+1])

def check_diags(puzz, coords):
    # check diags one way
    for start in range(len(puzz[0])):
        diag = ''
        locs = []
        i = 0
        j = start 
        while j >= 0 and i <= len(puzz):
            diag += puzz[i][j]
            locs.append((i, j))
            i += 1
            j -= 1
        # print(diag)
        string_occurrences(diag, coords, locs),

    for start in range(1, len(puzz)):
        diag = ''
        locs = []
        i = len(puzz[0])-1
        j = start 
        while i >= 0 and j <= len(puzz)-1:
            #print(i, j, len(puzzle), len(puzzle[0]))
            diag += puzz[i][j]
            locs.append((i, j))
            i -= 1
            j += 1
        # print(diag)
        string_occurrences(diag, coords, locs)

# diags
check_diags(puzzle, a_coords)
check_diags(puzzle[::-1], b_coords)

for coord in b_coords:
    c = (len(puzzle) - 1 - coord[0], coord[1])
    if c in a_coords:
        count += 1

print('Part 2')
print(count)