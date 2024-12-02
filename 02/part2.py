def is_report_safe(r) -> bool:
    # Determine if increasing or decreasing based on first 2 levels
    first_lvl_diff = r[1] - r[0]
    increasing = None
    if first_lvl_diff >= 1 and first_lvl_diff <= 3:
        increasing = True
    elif first_lvl_diff <= -1 and first_lvl_diff >= -3:
        increasing = False

    # if it is not increasing or decreasing by the specified rules, this report isn't safe
    if increasing is None:
        return False

    # now process rest with the knowledge of the increasing/decreasing pattern
    for lvl in range(1, len(r)-1):
        lvl_diff = r[lvl+1] - r[lvl]
        
        # if safe condition isn't met -> return False
        if increasing and not (lvl_diff >= 1 and lvl_diff <= 3):
            return False
        elif not increasing and not (lvl_diff <= -1 and lvl_diff >= -3):
            return False

    # if no unsafe levels have been detected thus far, we have a safe report
    return True

puzzle_input = open('./02/input', encoding='utf-8').read().splitlines()

num_of_safe_reports = 0
for report in puzzle_input:
    levels = [int(x) for x in report.split(' ')]
    for x in range(len(levels)):
        level_to_inspect = levels[:x] + levels[x+1:]
        if is_report_safe(level_to_inspect):
            num_of_safe_reports += 1
            break

print('Part 2:')
print(num_of_safe_reports)



    


