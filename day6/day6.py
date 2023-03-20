import sys
sys.path.insert(0, r'C:\Users\Donát\Documents\GitHub\AdventOfCode\functions')
from read_in import *

raw_signal_input = read_lines_in(r"C:\Users\Donát\Documents\GitHub\AdventOfCode\day6\input.txt")[0]

marker = []
for index, char in enumerate(raw_signal_input):
    temp = []
    marker.append(char)
    if index > 3:
        marker.pop(0)
    temp = [*set(marker)]
    if len(temp) == 4:
        print(index + 1)
        break