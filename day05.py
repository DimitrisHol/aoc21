arraySize = 1000 # 10 for test, 1000 for input


def printVentArray(ventArray) : 
        arrayToPrint = []
        for line in ventArray : 
            newLine = []
            for character in line : 
                if character == 0 : 
                    newLine.append(".")
                else : 
                    newLine.append(str(character))
            arrayToPrint.append(newLine)


        for line in arrayToPrint : 
            print(line)
            
def part1() : 

    # ventArray = [[0] * arraySize] * arraySize don't use this lol it's reference
    ventArray = [ [0] * arraySize for i in range(arraySize)]

    with open("input/day05.txt") as file : 
        

        for line in file : 
            inputLine = line.rstrip().split(" -> ")

            startPoint = inputLine[0].split(",")    # (x1,y1)
            finishPoint = inputLine[1].split(",")   # (x2,y2)

            # Cast to int, it looks horrible later. 
            for i in range(len(startPoint)) : 
                startPoint[i] = int(startPoint[i])
                finishPoint[i] = int(finishPoint[i])

            x1 = startPoint[0]
            x2 = finishPoint[0]

            y1 = startPoint[1]
            y2 = finishPoint[1]

            maxX = max (x1,x2)
            minX = min(x1,x2)

            maxY = max(y1,y2)
            minY = min(y1,y2)

            if x1 == x2 : 
                for i in range(minY,maxY+1) : 
                    ventArray[i][x1] += 1
            elif y1 == y2 : 
                for i in range(minX,maxX+1) : 
                    ventArray[y1][i] += 1

        count = 0
        for line in ventArray : 
            for number in line : 
                if number >= 2 : 
                    count +=1

        print("Total Count for part 1 :", count)

def part2() : 

    ventArray = [ [0] * arraySize for i in range(arraySize)]
    with open("input/day05.txt") as file : 

        for line in file : 
            inputLine = line.rstrip().split(" -> ")

            startPoint = inputLine[0].split(",")    # (x1,y1)
            finishPoint = inputLine[1].split(",")   # (x2,y2)

            # Cast to int, it looks horrible later. 
            for i in range(len(startPoint)) : 
                startPoint[i] = int(startPoint[i])
                finishPoint[i] = int(finishPoint[i])

            x1 = startPoint[0]
            x2 = finishPoint[0]

            y1 = startPoint[1]
            y2 = finishPoint[1]

            maxX = max (x1,x2)
            minX = min(x1,x2)

            maxY = max(y1,y2)
            minY = min(y1,y2)

            if x1 == x2 : 
                for i in range(minY,maxY+1) : 
                    ventArray[i][x1] += 1
            elif y1 == y2 : 
                for i in range(minX,maxX+1) : 
                    ventArray[y1][i] += 1
            else : 
                # The angle is always diagonal, 45 degrees. 
                # If the angle = 1, as x increases, y increases --> top to bottom 
                # if the angle = -1, as the x increases, y decreases or, as y increases x decreases.

                # For angle = 1, we start from min x, min Y and  each time x+1 , y + 1
                # For angle = -1, we start from min x, max Y each time x +1, y - 1
                
                angle = (y2 - y1) / (x2 - x1)
                # print(x1, y1, x2, y2, angle)

                x = minX
                if angle == 1 : 
                    y = minY
                else : 
                    y = maxY

                # Filling everything in : 

                for i in range(maxX - minX + 1) : 
                    ventArray[y][x] += 1    # You need to flip x/y because of how the puzzle considers the axis. 

                    x += 1
                    if angle == 1 : 
                        y += 1
                    else : 
                        y -= 1

        # printVentArray(ventArray)

        count = 0
        for line in ventArray : 
            for number in line : 
                if number >= 2 : 
                    count +=1

        print("Total Count for part 2 :", count)

def part3() : 

    ventArrayPart1 = []
    ventArrayPart2 = []

    with open("input/test/part2.txt") as file2 : 

        for line in file2 : 

            ventArrayPart2.append(list(line.strip()))
            
    with open("input/test/part1.txt") as file1 : 

        for line in file1 : 

            ventArrayPart1.append(list(line.strip()))

    newBoard = []

    for i in range(len(ventArrayPart1)) : 

        newLine = []

        for j in range(len(ventArrayPart1[i])) : 

            part1 = ventArrayPart1[i][j]
            part2 = ventArrayPart2[i][j] 

            if part1 == '.' and part2 == '.' : 
                newLine.append(".")
            elif part1 == '.' : 
                newLine.append(part2)
            else : 
                difference = int(part2) - int(part1)
                if difference == 0 : 
                    newLine.append(".")
                else : 
                    newLine.append(str(difference))
        newBoard.append(newLine)

    print("we should be printing this ")
    for line in newBoard : 
        print(line)


part1()
part2() 
# part3()

