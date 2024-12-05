from pprint import pprint


puzzle = open('./04/input', encoding='utf-8').read().splitlines()

WORD = 'XMAS'
WORD_LEN = len(WORD)
count = 0

def is_xmas(word):
    return word == WORD or word[::-1] == WORD

def string_occurrences(s):
    result = 0
    for c in range(len(s)-WORD_LEN+1):
        candidate = s[c:c+4]
        
        if is_xmas(candidate):
            result += 1
    return result

def check_diags(puzz):
    result = 0
    # check diags one way
    for start in range(len(puzz[0])):
        diag = ''
        i = 0
        j = start 
        while j >= 0 and i <= len(puzz):
            diag += puzz[i][j]
            i += 1
            j -= 1
        # print(diag)
        result += string_occurrences(diag)

    for start in range(1, len(puzz)):
        diag = ''
        i = len(puzz[0])-1
        j = start 
        while i >= 0 and j <= len(puzz)-1:
            #print(i, j, len(puzzle), len(puzzle[0]))
            diag += puzz[i][j]
            i -= 1
            j += 1
        # print(diag)
        result += string_occurrences(diag)
    return result

# check rows
for row in puzzle:
    count += string_occurrences(row)

# check columns
for col_num in range(len(puzzle[0])):
    col = ''.join([row[col_num] for row in puzzle])
    count += string_occurrences(col)

# diags
count += check_diags(puzzle)
count += check_diags(puzzle[::-1])

print('Part 1')
print(count)