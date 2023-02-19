with open(r"C:\Users\Donát\Documents\GitHub\AdventOfCode\day1\input.txt") as f:
    content = f.read()

numArray = []
temp = ''

for i in range(len(content)):
    if '\n' in content[i] and '\n' in content[i - 1]:
        numArray.append(0)
    elif '\n' in content[i]:
        numArray.append(int(temp))
        temp = ''
    else:
        temp += content[i]
numArray.append(int(temp))

maxSum = 0
tempSum = 0
for i in range(len(numArray)):
    if numArray[i] != 0:
        tempSum += numArray[i]
    else:
        if tempSum > maxSum:
            maxSum = tempSum
        tempSum = 0
       
print(maxSum)