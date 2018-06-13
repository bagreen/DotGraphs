def hasNumbers(input):
    return any(char.isdigit() for char in input)

with open('notDotCount.txt') as f:
    totalNumber = 0
    for line in f:
        number = line
        number = int(number)
        totalNumber = totalNumber + number
    print totalNumber