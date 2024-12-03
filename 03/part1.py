puzzle_input = open('./03/input', encoding='utf-8').read()

candidate_indexes = []

# scan with a window of 4 characters through input to find
# potential commandes
for x in range(len(puzzle_input)-1-4):
    if puzzle_input[x:x+4] == 'mul(':
        candidate_indexes.append(x)

# now lets vet these candidates more
sum_of_mults = 0
for i in candidate_indexes:
    scan_index = i + 4
    
    # attempt to read first number
    first_number = ''
    while puzzle_input[scan_index] in '0123456789':
        first_number += puzzle_input[scan_index]
        scan_index += 1
    
    # now check for comma
    if puzzle_input[scan_index] == ',':
        scan_index += 1
    else:
        continue

    # now attempt to read second number
    second_number = ''
    while puzzle_input[scan_index] in '0123456789':
        second_number += puzzle_input[scan_index]
        scan_index += 1
    
    # now check for closing parentsthe
    if puzzle_input[scan_index] == ')':
        scan_index += 1
    else:
        continue

    # we made it this far now lets do the mult
    # operation and add to final result
    sum_of_mults += int(first_number) * int(second_number)

print('Part 1:')
print(sum_of_mults)
