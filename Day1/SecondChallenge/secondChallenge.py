### Second challenge



# Get the input from the file
def readData():
    dataFile = open("./Day1/FirstChallenge/input.txt")
    inputList = []
    for line in dataFile:
        thisLine = line.split(" ")
        inputList.append(int(thisLine[0]))
    dataFile.close()
    return inputList

inputArray = readData()
print(len(inputArray))

newArray = []
i = 0
while i < len(inputArray):
    if (i + 3) > len(inputArray):
        break
    threeAdded = inputArray[i] + inputArray[i + 1] + inputArray[i + 2]
    
    newArray.append(threeAdded)
    i += 1
print(newArray)


count = 0
isBiggerCount = 0
for i in range(len(newArray)):
    count += 1
    if newArray[i] > newArray[i - 1]:
        isBiggerCount += 1

print(f"Answer is: {isBiggerCount}")


# Answer = 1575