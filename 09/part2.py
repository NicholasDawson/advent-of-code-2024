from pprint import pprint


puzzle_input = open('./09/input', encoding='utf-8').read()

# list format = file blocks, free space blocks, ...
system = []
x = 0
id = 0
while x < len(puzzle_input):
    system.append([id, int(puzzle_input[x])]) # file block
    if x+1 < len(puzzle_input):
        system.append([None, int(puzzle_input[x+1])]) # free space block
    x += 2 # skip to next section
    id += 1 # increment to next ID

# print(system)

# now we built the blocks (system) lets do the file compacting process
index = len(system) - 1
id -= 1
while index >= 0:
    to_move = (system[index][0], system[index][1]) # get last item
    # print(f'trying to move {to_move[0]}')

    # if we grab actual data let's move it to the first available free space chunk
    if to_move[0] == id:
        id -= 1
        for x in range(len(system)):
            if x >= index:
                break
            # once we find a free space
            if system[x][0] is None and system[x][1] >= to_move[1]:
                # print('moved.')
                diff = system[x][1] - to_move[1]
                system[index][0] = None # replace previous location to free space
                system.insert(x, [to_move[0], to_move[1]]) # move to free space
                system[x+1][1] = diff # reduce size of free space
                break
        
    # increment to get next index
    index -= 1

#     for x in system:
#         if x[0] is None:
#             print('.' * x[1], end='')
#         else:
#             print(str(x[0]) * x[1], end='')
#     print()

# print(system)

# for x in system:
#     if x[0] is None:
#         print('.' * x[1], end='')
#     else:
#         print(str(x[0]) * x[1], end='')
# print()

# now calculate the checksum
checksum = 0
id = 0
for x in range(len(system)):
    for _ in range(system[x][1]):
        if system[x][0] is not None:
            checksum += id * system[x][0]
        id += 1

print('Part 2')
print(checksum)
