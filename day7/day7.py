import sys
sys.path.insert(0, r'C:\Users\Donát\Documents\GitHub\AdventOfCode\functions')
from read_in import *

class Folder():
    def __init__(self, name, root = None):
        self.name = name
        self.parent = root
        self.subfolders = []
        self.size = 0
        self.small_folder = True
    
    def add_subfolder(self, subfolder):
        self.subfolders.append(subfolder)

    def add_size(self, file_size):
        self.size += file_size
        if self.size > 100000:
            self.small_folder = False
        if self.parent:
            self.parent.add_size(file_size)

    def small_folders(self, folders):
        for subfolder in self.subfolders:
            subfolder.small_folders(folders)
        if self.small_folder:
            folders.append(self.size)
        return folders            

terminal_input = read_sentences_in(r"C:\Users\Donát\Documents\GitHub\AdventOfCode\day7\input.txt")

init_root_folder = terminal_input[0]
terminal_input.pop(0)
root_dir = Folder(init_root_folder[2])
current_dir = root_dir

for index, command in enumerate(terminal_input):
    if command[0] == '$':
        if command[1] == 'cd':
            if command[2] == '..':
                current_dir = current_dir.parent
            else:
                temp = Folder(command[2], current_dir)
                current_dir.add_subfolder(temp)
                current_dir = temp
    elif command[0].isnumeric():
        current_dir.add_size(int(command[0]))

small_folders = []    
root_dir.small_folders(small_folders) 
small_folder_size_sum = 0
for folder in small_folders:
    small_folder_size_sum += folder
print(small_folder_size_sum)