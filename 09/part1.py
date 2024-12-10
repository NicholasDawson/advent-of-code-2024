from pprint import pprint


puzzle_input = open('./09/input', encoding='utf-8').read()

# list format = file blocks, free space blocks, ...
system = []
x = 0
id = 0
while x < len(puzzle_input):
    system += [id] * int(puzzle_input[x]) # file block
    if x+1 < len(puzzle_input):
        system += [None] * int(puzzle_input[x+1]) # free space block
    x += 2 # skip to next section
    id += 1 # increment to next ID

print(system)

# now we built the blocks (system) lets do the file compacting process
while True:
    to_move = system.pop() # grab last item
    if to_move is not None:
        # if we grab actual data let's move it to the first available free space
        found_spot = False
        for x in range(len(system)):
            # once we find a free space
            if system[x] is None:
                system[x] = to_move
                found_spot = True
                break
        if not found_spot:
            system.append(to_move)
            break

print(system)

# now calculate the checksum
checksum = 0
for x in range(len(system)):
    checksum += x * system[x]

print('Part 1')
print(checksum)
