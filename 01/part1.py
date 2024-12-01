puzzle_input = open('./01/input', encoding='utf-8').read().splitlines()

list1 = []
list2 = []
for line in puzzle_input:
    num1, num2 = line.split('   ')
    list1.append(int(num1))
    list2.append(int(num2))

list1 = sorted(list1)
list2 = sorted(list2)

diffs = 0
for x in range(len(list1)):
    diffs += abs(list1[x] - list2[x])

print('Part 1:')
print(diffs)
