def part1() :

    with open("input/test/day04.txt") as file : 

        bingoNumbers, bingoBoards = parseBingoInput(file)

        print(bingoNumbers)
        # printBingoBoards(bingoBoards)
        for drawnNumber in bingoNumbers : 
            for board in bingoBoards : 
                markNumberAtBoard(drawnNumber, board)
            break
                
        # print("----- AFTER -----")
        # printBingoBoards(bingoBoards)


def markNumberAtBoard(drawnNumber, board) : 

    for line in board : 
        for boardNumber in line : 
            if boardNumber[0] == drawnNumber : 
                boardNumber[1] = 1
        

def parseBingoInput(file) : 

    # Read the first row, get the numbers
    bingoNumbers = file.readline().rstrip().split(",")

    bingoNumbers = [int(x) for x in bingoNumbers]

    bingoBoard = []
    bingoBoards = []
    for line in file :
        
        if line == '\n' : 
            if (bingoBoard) : 
                cleanBoard = cleanUpBoard(bingoBoard)
                bingoBoards.append(cleanBoard)
            bingoBoard = []
        else : 
            bingoBoard.append(line.rstrip().split(" "))

    # Add the last board to to the list     
    cleanBoard = cleanUpBoard(bingoBoard)
    bingoBoards.append(cleanBoard)
        
    return bingoNumbers, bingoBoards


def cleanUpBoard(bingoBoard) : 

    newBingoBoard = []

    for line in bingoBoard : 

        line = [[int(number), 0] for number in line if number != '']
        newBingoBoard.append(line)

    return newBingoBoard


def printBingoBoards(bingoBoards) : 

    for bingoBoard in bingoBoards : 

            print("new board")

            for line in bingoBoard :
                print(line)

part1()


