stones = open('./11/input', encoding='utf-8').read()
stones = [int(x) for x in stones.split()]

for i in range(75):
    print(i)
    s = 0
    while s < len(stones):
        stone = stones[s]
        strstone = str(stone)
        
        if stone == 0:
            stones[s] = 1
        # if len is even    
        elif len(strstone) % 2 == 0:
            halflen = int(len(strstone)/2)
            s1, s2 = int(strstone[:halflen]), int(strstone[halflen:])
            stones[s] = s2
            stones.insert(s, s1)
            s += 1
        else:
            stones[s] *= 2024
        
        s += 1

print('Part1')
print(len(stones))
