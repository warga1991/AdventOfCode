import sys
sys.path.insert(0, r'C:\Users\Donát\Documents\GitHub\AdventOfCode\functions')
from read_in import *

container_stack_lines = []
mf = open(r"C:\Users\Donát\Documents\GitHub\AdventOfCode\day5\input_containers.txt", 'r+')
for line in mf:
    temp = [*line]
    removeable_space_index = []
    for index in range(len(temp)):
        if index % 2 == 0:
            removeable_space_index.append(index)
        if index % 4 == 3:
            removeable_space_index.append(index)
    for index in reversed(removeable_space_index):
        temp.pop(index)
    container_stack_lines.append(temp)
mf.close()
#print(container_stack_lines)

reversed_container_stack_lines = list(reversed(container_stack_lines))
reversed_container_stack_lines.pop(0) # remove number line
container_stacks = []
for horizontal_container_reading in reversed_container_stack_lines:
    for index, cargo in enumerate(horizontal_container_reading):
        if len(container_stacks) <= len(reversed_container_stack_lines):
            container_stacks.append([cargo])
        else:
            container_stacks[index].append(cargo)
for cargo in container_stacks:
    while ' ' in cargo:
        cargo.remove(' ')
[print(stack) for stack in container_stacks]

command_array = read_sentences_in(r"C:\Users\Donát\Documents\GitHub\AdventOfCode\day5\input_commands.txt")

print(container_stacks)
for command in command_array:
    for i in range(3):
        command.pop(i)
        command[i] = int(command[i])
for command in command_array:
    cargo_num = command[0]
    cargo_origin = command[1] - 1
    cargo_destination = command[2] - 1
    for i in range(cargo_num):
        container_stacks[cargo_destination].append(container_stacks[cargo_origin][-1])
        container_stacks[cargo_origin].pop()

tops = ''
for stack in container_stacks:
    reversed_stack = list(reversed(stack))
    tops += reversed_stack[0]
print(tops)