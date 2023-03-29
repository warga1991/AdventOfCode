import sys
sys.path.insert(0, r'C:\Users\Donát\Documents\GitHub\AdventOfCode\functions')
from read_in import *
import numpy as np

forest = read_lines_in_separated(r"C:\Users\Donát\Documents\GitHub\AdventOfCode\day8\input.txt")
forest = [[int(tree) for tree in treeline]for treeline in forest]

np_forest = np.zeros((len(forest), len(forest[0])))

for i, treeline in enumerate(forest):
    for j, tree in enumerate(treeline):
        np_forest[i, j] = tree

np_forest_t = np.transpose(np_forest)

visible_tree_cnt = 0
for i, treeline in enumerate(np_forest):
    for j, tree in enumerate(treeline):
        treeline_left = np.array(treeline[:j])
        treeline_right = np.array(treeline[j+1:])
        treeline_upper = np.array(np_forest_t[j][:i])
        treeline_lower = np.array(np_forest_t[j][i+1:])
        tree_on_side = treeline_left.size == 0 or treeline_right.size == 0 or treeline_upper.size == 0 or treeline_lower.size == 0
        if tree_on_side:
            visible_tree_cnt += 1
        else:
            visible_tree = tree > treeline_left.max() or tree > treeline_right.max() or tree > treeline_upper.max() or tree > treeline_lower.max()
            if visible_tree:
                visible_tree_cnt += 1

print(visible_tree_cnt)