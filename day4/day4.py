import sys
sys.path.insert(0, r'C:\Users\Donát\Documents\GitHub\AdventOfCode\functions')
from read_in import read_lines_in

raw_input_array = read_lines_in(r"C:\Users\Donát\Documents\GitHub\AdventOfCode\day4\input.txt")
working_pairs_processed = list(map(lambda x: x.split(','), raw_input_array))

not_overlaping_cnt = 0
for working_pair in working_pairs_processed:
    first_worker = [int(i) for i in working_pair[0].split('-')]
    second_worker = [int(i) for i in working_pair[1].split('-')] 
    first_worker_first_task, first_worker_second_task = first_worker[0], first_worker[1]
    second_worker_first_task, second_worker_second_task = second_worker[0], second_worker[1]
    if first_worker_first_task > second_worker_second_task or second_worker_first_task > first_worker_second_task:
        not_overlaping_cnt += 1
print(len(working_pairs_processed) - not_overlaping_cnt)