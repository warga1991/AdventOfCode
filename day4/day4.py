import sys
sys.path.insert(0, r'C:\Users\Donát\Documents\GitHub\AdventOfCode\functions')
from read_in import read_lines_in

raw_input_array = read_lines_in(r"C:\Users\Donát\Documents\GitHub\AdventOfCode\day4\input.txt")
working_pairs_processed = list(map(lambda x: x.split(','), raw_input_array))

overlap_cnt = 0
for working_pair in working_pairs_processed:
    first_worker = working_pair[0].split('-')
    second_worker = working_pair[1].split('-')
    first_inside_second = int(first_worker[0]) >= int(second_worker[0]) and int(first_worker[1]) <= int(second_worker[1])
    second_inside_first = int(first_worker[0]) <= int(second_worker[0]) and int(first_worker[1]) >= int(second_worker[1])
    if first_inside_second or second_inside_first:
        overlap_cnt += 1

print(overlap_cnt)