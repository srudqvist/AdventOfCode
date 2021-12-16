# Challenge 1 Day 3
# https://adventofcode.com/2021/day/3



# Get the input from the file
def readData():
    dataFile = open("./Day3/ShortInput.txt")
    inputList = []
    inputList2 = []
    inputList3 = []
    inputList4 = []
    inputList5 = []
    for line in dataFile:
        inputList.append(int(line[0]))
        inputList2.append(int(line[1]))
        inputList3.append(int(line[2]))
        inputList4.append(int(line[3]))
        inputList5.append(int(line[4]))
    dataFile.close()
    return inputList, inputList2, inputList3, inputList4, inputList5


def count():
    list, list2, list3, list4, list5 = readData()
    gammaList = []
    epsilonList = []
    one = 0
    zero = 0
    for i in range(len(list)):
        if list[i] == 0:
            zero += 1
        else:
            one += 1
    print(f"Zero: {zero}")    
    print(f"One: {one}")
    gammaList.append()
    
    return zero, one

count()