from collections import Counter
from copy import deepcopy

stones = open('./11/input', encoding='utf-8').read()
stones = Counter([int(x) for x in stones.split()])

for i in range(1000):
    #print(i, len(stones))
    new_stones = Counter()
    for s in stones:
        strstone = str(s)
        
        if s == 0:
            new_stones[1] += stones[s]
        # if len is even    
        elif len(strstone) % 2 == 0:
            halflen = int(len(strstone)/2)
            s1, s2 = int(strstone[:halflen]), int(strstone[halflen:])
            new_stones[s1] += stones[s]
            new_stones[s2] += stones[s]
        else:
            new_stones[s * 2024] += stones[s]
    stones = new_stones
        

print('Part2')
print(stones.total())
