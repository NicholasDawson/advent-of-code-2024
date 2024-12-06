from pprint import pprint
from typing import List


puzzle_input = open('./05/input', encoding='utf-8').read().splitlines()

class Rule:
    def __init__(self, rule_string):
        nums = rule_string.split('|')
        self.first = int(nums[0])
        self.second = int(nums[1])

    def rule_applies(self, update: List[int]):
        return self.first in update and self.second in update

    def __repr__(self):
        return f'{self.first}|{self.second}'


# READ IN THE RULES AND UPDATES FROM INPUT

rules: List[Rule] = []
updates = []

reading_rules = True
for line in puzzle_input:
    if line == '':
        reading_rules = False
        continue

    if reading_rules:
        rules.append(Rule(line))
    else:
        updates.append([int(x) for x in line.split(',')])

# CHECK VALID UPDATES
result = 0
invalid_updates = []
for u in updates:
    invalid = False
    for page in range(len(u)):
        for rule in rules:
            # if the rule applies and the 
            if rule.rule_applies(u[page:]) and rule.second == u[page]:
                invalid = True
                break
        if invalid:
            break
    if not invalid:
        #print('valid', u)
        #print('adding: ', u[int(len(u)/2)])
        result += u[int(len(u)/2)]
    else:
        invalid_updates.append(u)

# now process invalid updates

