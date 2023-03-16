import sys
sys.path.insert(0, r'C:\Users\Donát\Documents\GitHub\AdventOfCode\functions')
from read_in import *

result_array = []
mf = open(r"C:\Users\Donát\Documents\GitHub\AdventOfCode\day5\input_containers.txt", 'r+')
for line in mf:
    temp = [*line]
    removeable_space_index = []
    for index in range(len(temp)):
        if temp[index] == ' ' and index % 2 == 0:
            removeable_space_index.append(index)
    for index in reversed(removeable_space_index):
        temp.pop(index)
    while '[' in temp:
        temp.remove('[')
        temp.remove(']')
    removeable_space_index = []
    for index in range(len(temp)):
        if index % 2 == 1:
            removeable_space_index.append(index)
    for index in reversed(removeable_space_index):
        temp.pop(index)
    #print(line, temp)
    result_array.append(temp)
    print(temp)
mf.close()

#raw_command_array = read_sentences_in(r"C:\Users\Donát\Documents\GitHub\AdventOfCode\day5\input_commands.txt")