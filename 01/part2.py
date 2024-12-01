puzzle_input = open('./01/input', encoding='utf-8').read().splitlines()

list1 = []
list2 = []
for line in puzzle_input:
    num1, num2 = line.split('   ')
    list1.append(int(num1))
    list2.append(int(num2))

list1 = sorted(list1)
list2 = sorted(list2)

list2_counts = {}
for x in list2:
    if x in list2_counts:
        list2_counts[x] += 1
    else:
        list2_counts[x] = 1

score = 0
for x in list1:
    if x in list2_counts:
        score += (x * list2_counts[x])

print('Part 2:')
print(score)
