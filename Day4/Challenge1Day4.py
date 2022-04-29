# Challenge 1 Day 4

class Bingo:
    def __init__(self, number):
        self.number = number
    
    def read_order(self):
        data_file = open("./Day4/shortInput.txt")
        play_order = []
        for line in data_file:
            # Split the input file into one line
            first_line = line.strip().split("\n")
            # Split the one line into single two digit numbers
            character = first_line[0].split(",")
            # Loop through the list of single two digit numbers, add them as integers 
            # to the play order list
            for i in range(len(character)):
                play_order.append(int(character[i]))
            # Break the loop after the first line
            break        
            
        data_file.close()
        print(play_order)
        return play_order


# The Board class takes a position and a number as parameters.
class Board:
    def __init__(self, position, number):
        self.position = position
        self.number = number
    
    def set_values(self, position, number):
        data_file = open("./Day4/shortInput.txt")
        board = []
        for line in data_file:
            if line.__contains__("83,69,34,46,30,23,19,75,22,37,89,78,32,39,11,44,95,43,26,48,84,53,94,88,18,40,62,35,27,42,15,2,91,20,4,64,99,71,54,97,52,36,28,7,74,45,70,86,98,1,61,50,68,6,77,8,57,47,51,72,65,3,49,24,79,13,17,92,41,80,63,67,82,90,55,0,10,93,38,21,59,73,33,31,9,76,5,66,16,58,85,87,12,29,25,14,96,56,60,81"):
                pass
            else:
                curr_line = line.split("\n")
                print(f"line: {line}")
                print(f"curr_line0: {curr_line}")
                for i in range(1, len(curr_line)):
                    curr_line = curr_line[0].split(",")
                    curr_line = curr_line[0].split(" ")

                    for i in range(len(curr_line)):
                        if curr_line == " ":
                            pass
                        elif curr_line[i] == '':
                            pass
                        else:
                            print(curr_line[i])
                            board.append(int(curr_line[i]))
               
                    print(f"curr_line: {curr_line}")
        data_file.close()
        print(board)


    def get_values(self):
        pass

    def is_match(self):
        pass
    

if __name__ == '__main__':
    order = Bingo.read_order(1)
    board = Board.set_values(1, 1, 1)
