# Challenge 1 Day 3
# https://adventofcode.com/2021/day/3



# Get the input from the file
def readData():
    dataFile = open("./Day3/input.txt")
    inputList = []
    inputList2 = []
    inputList3 = []
    inputList4 = []
    inputList5 = []
    inputList6 = []
    inputList7 = []
    inputList8 = []
    inputList9 = []
    inputList10 = []
    inputList11 = []
    inputList12 = []
    for line in dataFile:
        inputList.append(int(line[0]))
        inputList2.append(int(line[1]))
        inputList3.append(int(line[2]))
        inputList4.append(int(line[3]))
        inputList5.append(int(line[4]))
        inputList6.append(int(line[5]))
        inputList7.append(int(line[6]))
        inputList8.append(int(line[7]))
        inputList9.append(int(line[8]))
        inputList10.append(int(line[9]))
        inputList11.append(int(line[10]))
        inputList12.append(int(line[11]))
    dataFile.close()
    return inputList, inputList2, inputList3, inputList4, inputList5, inputList6, inputList7, inputList8, inputList9, inputList10, inputList11, inputList12

# count() - loop through each of the positions in the inputLists and record if the most
#           common one is a 1 or 0.
def count():
    list, list2, list3, list4, list5, list6, list7, list8, list9, list10, list11, list12 = readData()
    gammaList = []
    epsilonList = []
    one = 0
    zero = 0
    for i in range(len(list)):
        if list[i] == 0:
            zero += 1
        else:
            one += 1
    if one > zero:
        gammaList.append(1)
        epsilonList.append(0)
    else:
        gammaList.append(0)
        epsilonList.append(1)

    one = 0
    zero = 0
    for i in range(len(list2)):
        if list2[i] == 0:
            zero += 1
        else:
            one += 1
    if one > zero:
        gammaList.append(1)
        epsilonList.append(0)
    else:
        gammaList.append(0)
        epsilonList.append(1)

    one = 0
    zero = 0
    for i in range(len(list3)):
        if list3[i] == 0:
            zero += 1
        else:
            one += 1
    if one > zero:
        gammaList.append(1)
        epsilonList.append(0)
    else:
        gammaList.append(0)
        epsilonList.append(1)
    
    one = 0
    zero = 0
    for i in range(len(list4)):
        if list4[i] == 0:
            zero += 1
        else:
            one += 1
    if one > zero:
        gammaList.append(1)
        epsilonList.append(0)
    else:
        gammaList.append(0)
        epsilonList.append(1)
    
    one = 0
    zero = 0
    for i in range(len(list5)):
        if list5[i] == 0:
            zero += 1
        else:
            one += 1
    if one > zero:
        gammaList.append(1)
        epsilonList.append(0)
    else:
        gammaList.append(0)
        epsilonList.append(1)
    
    one = 0
    zero = 0
    for i in range(len(list6)):
        if list6[i] == 0:
            zero += 1
        else:
            one += 1
    if one > zero:
        gammaList.append(1)
        epsilonList.append(0)
    else:
        gammaList.append(0)
        epsilonList.append(1)
    
    one = 0
    zero = 0
    for i in range(len(list7)):
        if list7[i] == 0:
            zero += 1
        else:
            one += 1
    if one > zero:
        gammaList.append(1)
        epsilonList.append(0)
    else:
        gammaList.append(0)
        epsilonList.append(1)
    
    one = 0
    zero = 0
    for i in range(len(list8)):
        if list8[i] == 0:
            zero += 1
        else:
            one += 1
    if one > zero:
        gammaList.append(1)
        epsilonList.append(0)
    else:
        gammaList.append(0)
        epsilonList.append(1)
        
    
    one = 0
    zero = 0
    for i in range(len(list9)):
        if list9[i] == 0:
            zero += 1
        else:
            one += 1
    if one > zero:
        gammaList.append(1)
        epsilonList.append(0)
    else:
        gammaList.append(0)
        epsilonList.append(1)
    
    one = 0
    zero = 0
    for i in range(len(list10)):
        if list10[i] == 0:
            zero += 1
        else:
            one += 1
    if one > zero:
        gammaList.append(1)
        epsilonList.append(0)
    else:
        gammaList.append(0)
        epsilonList.append(1)
    
    one = 0
    zero = 0
    for i in range(len(list11)):
        if list11[i] == 0:
            zero += 1
        else:
            one += 1
    if one > zero:
        gammaList.append(1)
        epsilonList.append(0)
    else:
        gammaList.append(0)
        epsilonList.append(1)
    
    one = 0
    zero = 0
    for i in range(len(list12)):
        if list12[i] == 0:
            zero += 1
        else:
            one += 1
    if one > zero:
        gammaList.append(1)
        epsilonList.append(0)
    else:
        gammaList.append(0)
        epsilonList.append(1)

    
    print(f"gammaList: {gammaList} \nepsilonList {epsilonList}")
    return gammaList, epsilonList

# toDecimal() - takes a binary list and returns the decimal value
#   Parameters:
#       binaryList - the gammaList and epsilonList from the count function.
def toDecimal(binaryList):
    gammaList = binaryList[0]
    epsilonList = binaryList[1]
    gammaDecimal = 0
    epsilonDecimal = 0

    for i in range (len(gammaList)):
        if gammaList[i] == 1:
            gammaDecimal += 2 ** (11-i)

    for i in range (len(epsilonList)):
        if epsilonList[i] == 1:
            epsilonDecimal += 2 ** (11-i)

    print(f"gammaDecimal: {gammaDecimal} \nepsilonDecimal: {epsilonDecimal}")
    return gammaDecimal, epsilonDecimal

def main():
    gammaDecimal, epsilonDecimal = toDecimal(count())
    powerConsumption = gammaDecimal * epsilonDecimal
    print(f"\npowerConsumption: {powerConsumption}")

### Answer: short input 198, long input 4118544
# bad code, must change a lot if the length of each line in the input is different.
main()
