def part1() :

    with open("input/day04.txt") as file : 

        bingoNumbers, bingoBoards = parseBingoInput(file)

        # bingoNumbers = [22, 8, 21, 6, 1]
        finalScore = 0

        for drawnNumber in bingoNumbers : 
            for board in bingoBoards : 
                markNumberAtBoard(drawnNumber, board)
                if checkForBingo(board) : 
                    print("BINGO")
                    finalScore = calculateScoreForBoard(drawnNumber, board)
                    break 
            else : 
                continue 
            break
                # Maybe check after putting the 5th number,
                # before there is no way that we got it lol
        print("Score for bingo is : ", finalScore)

def part2() : 

    with open("input/day04.txt") as file : 

        bingoNumbers, bingoBoards = parseBingoInput(file)
        # Mark each board if it gets a bingo with a True variable.
        # We should have probably used a Class? 
        markedBingoBoards = [[bingoBoard, False] for bingoBoard in bingoBoards]

        for drawnNumber in bingoNumbers : 
            for board in markedBingoBoards : 
                # Check only unmarked boards 
                if not board[1] : 
                    markNumberAtBoard(drawnNumber, board[0])
                    if checkForBingo(board[0]) : 
                        print("We have a bingo for this board!")
                        finalScore = calculateScoreForBoard(drawnNumber, board[0])
                        board[1] = True

        print("Score for bingo is : ", finalScore)

def calculateScoreForBoard(drawnNumber, board) : 

    totalSum = 0 
    for line in board : 
        for dictionary in line : 
            if dictionary[1] != 1 : 
                totalSum += dictionary[0]
    
    print("Unmarked numbers sum is ", totalSum, "last drawnNumber" , drawnNumber)
    print("Final score : ", totalSum * drawnNumber)
    return totalSum * drawnNumber


def checkForBingo(board) : 

    bingo = False

    # Check for all rows
    for line in board : 

        bingoCount = 0
        for dictionary in line : 
            if dictionary[1] == 1 : 
                bingoCount += 1
        
        if bingoCount == 5 :
            return True

    # Check for all columns 
    for j in range(5) : 

        bingoCount = 0 
        for i in range(5) : 
            if board[i][j][1] == 1 : 
                bingoCount += 1

        if (bingoCount == 5) : 
            print("Vertical Bingo !")
            return True

    return bingo


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
part2()
