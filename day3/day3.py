import sys
sys.path.insert(0, r'C:\Users\Donát\Documents\GitHub\AdventOfCode\functions')
from read_in import read_lines_in

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
first_container_array = list(map(lambda x: x[0:int(len(x)/2)], raw_input_array))
second_container_array = list(map(lambda x: x[int(len(x)/2):], raw_input_array))

priority_sum = 0
for i in range(len(first_container_array)):
    first_container = first_container_array[i]
    second_container = second_container_array[i]
    shared_items = []

    for first_container_item in first_container:
        if first_container_item in second_container:
            if first_container_item not in shared_items:
                shared_items.append(first_container_item)
            
    for item in shared_items:
        priority_sum += priority_values[item]
print(priority_sum)