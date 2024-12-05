from typing import List


puzzle_input = open('./05/example', encoding='utf-8').read().splitlines()

class Rule:
    def __init__(self, rule_string):
        nums = rule_string.split('|')
        self.x = int(nums[0])
        self.before = int(nums[1])

    def rule_applies(self, update: List[int]):
        return self.x in update and self.before in update

rules = []
updates = []

reading_rules = True
for line in puzzle_input:
    if line == '':
        reading_rules = False
        continue

    if reading_rules:
        rules.append(Rule(line))
    else:
        updates.append([int(x) for x in ])