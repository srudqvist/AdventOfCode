# Challenge 2 Day 2
# https://adventofcode.com/2021/day/2#part2


# Get the input from the file
def readData():
    dataFile = open("./Day2/input.txt")
    inputList = []
    for line in dataFile:
        thisLine = line.split(" ")
        inputList.append(thisLine[0])
        inputList.append(int(thisLine[1]))
    dataFile.close()
    return inputList

inputArray = readData()
print(inputArray)

def calculatePos(inputArray):
    horizPos = 0
    depth = 0
    aim = 0
    i = 0
    while i < len(inputArray):
        if (i + 1) > len(inputArray):
            break
        if inputArray[i] == "forward":
            horizPos += inputArray[i + 1]
            depth += aim * inputArray[i + 1]
        elif inputArray[i] == "up":
            aim -= inputArray[i + 1]
        elif inputArray[i] == "down":
            aim += inputArray[i + 1]
        i += 2
    print(horizPos * depth)
    return horizPos * depth

calculatePos(inputArray)

# small input should equal 150 (15*10) (horizontal * vertical)
