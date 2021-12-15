### The first advent of code challenge


# Get the input from the file
def readData():
    dataFile = open("./Day1/FirstChallenge/input.txt")
    inputList = []
    for line in dataFile:
        thisLine = line.split(" ")
        inputList.append(thisLine[0])
    dataFile.close()
    return inputList

inputArray = readData()
print(len(inputArray))


count = 0
isBiggerCount = 1
for i in range(len(inputArray)):
    count += 1
    print(inputArray[i-1])
    print(inputArray[i])
    if inputArray[i] > inputArray[i - 1]:
        isBiggerCount += 1

print(isBiggerCount)
print(count)