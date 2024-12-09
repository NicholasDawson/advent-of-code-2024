from dataclasses import dataclass
from pprint import pprint
from time import sleep
from typing import List

puzzle_input = open('./07/input', encoding='utf-8').read().splitlines()


def is_equation_true(result: int, numbers: List[int]) -> bool:
    # Base case, if math exceeds expected result those operators can't be right
    if numbers[0] > result:
        return False
    # additional base case, if length is 1, we can't do any more math, return if result is correct
    elif len(numbers) == 1:
        return numbers[0] == result
    
    # recursive case - addition
    add_result = is_equation_true(result, [numbers[0] + numbers[1]] + numbers[2:])
    mul_result = is_equation_true(result, [numbers[0] * numbers[1]] + numbers[2:])
    cat_result = is_equation_true(result, [int(str(numbers[0]) + str(numbers[1]))] + numbers[2:])

    return add_result or mul_result or cat_result


total = 0
for line in puzzle_input:
    # parse each line
    result, numbers = line.split(': ')
    result = int(result)
    numbers = [int(x) for x in numbers.split(' ')]

    # compute
    if is_equation_true(result, numbers):
        # print(result, numbers)
        total += result

print('Part 2')
print(total)
