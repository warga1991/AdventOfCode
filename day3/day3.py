import sys
sys.path.insert(0, r'C:\Users\Donát\Documents\GitHub\AdventOfCode\functions')
from read_in import read_lines_in
from itertools import combinations, permutations

abc_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

priority_values = {}
abc_length = len(abc_letters)
for i in range(2 * abc_length):
    if i >= abc_length:
        temp = abc_letters[i - abc_length].upper()
    else:
        temp = abc_letters[i]
    priority_values[temp] = i + 1

raw_input_array = read_lines_in(r"C:\Users\Donát\Documents\GitHub\AdventOfCode\day3\input.txt")

unique_items_backpack_array = []
for line in raw_input_array:
    unique_items = ''.join(set(line))
    sorted_unique_items = sorted(unique_items)
    unique_items_backpack_array.append(''.join(sorted_unique_items))

possible_backpack_combinations = list(combinations(unique_items_backpack_array, 3))

priority_sum = 0
matched_groups = []
for possible_group in possible_backpack_combinations:
    matching_item_cnt = 0
    badge = ''
    for item in possible_group[0]:
        if item in possible_group[1]:
            if item in possible_group[2]:
                badge = item
                matching_item_cnt += 1
    if matching_item_cnt == 1 and possible_group[0] not in matched_groups and possible_group[1] not in matched_groups and possible_group[2] not in matched_groups:
        priority_sum += priority_values[badge]
        for i in range(3):
            matched_groups.append(possible_group[i])
print(priority_sum)