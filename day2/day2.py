array = []

mf = open(r"C:\Users\Donát\Documents\GitHub\AdventOfCode\day2\input.txt", 'r+')
for line in mf:
    temp = [line[0], line[2]]
    array.append(line.split())
mf.close()


def score_fcn(opponent, me):
    score = 0
    res = { 'X': 0,
            'Y': 3,
            'Z': 6}
    val = { 'A': 1,
            'B': 2,
            'C': 3}
    score = res[me]
    if me == 'Y':
        score += val[opponent]
    elif me == 'Z':
        if opponent == 'C':
            score += 1
        else:
            score += val[opponent] + 1
    else:
        if opponent == 'A':
            score += 3
        else:
            score += val[opponent] - 1
    return score
    

result = 0
for i in range(len(array)):
    result += score_fcn(array[i][0], array[i][1])
print(result)