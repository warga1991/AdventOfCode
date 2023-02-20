array = []

mf = open(r"C:\Users\Donát\Documents\GitHub\AdventOfCode\day2\input.txt", 'r+')
for line in mf:
    temp = [line[0], line[2]]
    array.append(temp)
mf.close()



def score_fcn(opponent, me):
    score = 0
    win = { 'A': ['Y', 2],
            'B': ['Z', 3],
            'C': ['X', 1]}
    draw = { 'A': ['X', 1],
             'B': ['Y', 2],
             'C': ['Z', 3]}
    lose = { 'A': ['Z', 3],
             'B': ['X', 1],
             'C': ['Y', 2]}

    if me == win[opponent][0]:
        score = 6 + win[opponent][1] 
    elif me == draw[opponent][0]:
        score = 3 + draw[opponent][1]
    else:
        score = lose[opponent][1]

    return score
    

result = 0
for i in range(len(array)):
    result += score_fcn(array[i][0], array[i][1])
print(result)