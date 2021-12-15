arraySize = 10 # 10 for test, 1000 for input

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

        print(count)

def part2() : 

    ventArray = [ [0] * arraySize for i in range(arraySize)]
    with open("input/test/day05.txt") as file : 
        print("x1, y1, x2 , y2, angle")

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
                # for i in range(minY,maxY+1) : 
                    # ventArray[i][x1] += 1
                pass
            elif y1 == y2 : 
                # for i in range(minX,maxX+1) : 
                    # ventArray[y1][i] += 1
                pass
            else : 

                
                # 45 degrees mean angle is either 1 or -1 (DESC or ASC)
                # If the angle = -1 starting with the mixX pair, x++ ,y-- NorthEast, that means in the array = -x + y
                # If the angle = 1  starting with the minX pair, x++, y++ SouthEast, that means in the array = +x + y
                angle = (y2 - y1) / (x2 - x1)
                print(x1, y1, x2, y2, angle)

                # For the input x is horizontal, y is vertical
                # For us        x is vertical ,  y is horizontal

                x = minX # This means leftest possible in the array

                if angle == -1 : # This is upwards, so x--
                    y = maxY    # start from the bottom (maximum x)
                else :
                    y = minY    # start from the top since we're declining (incrementing x)

                for i in range(maxX - minX + 1) : 

                    ventArray[x][y] += 1
                    x += 1
                    if angle == -1 : 
                        y += 1
                    else : 
                        y -= 1

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
                

        count = 0
        for line in ventArray : 
            for number in line : 
                if number >= 2 : 
                    count +=1

        print("Total Count = ", count)

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

    for line in newBoard : 

        print(line)


# part1()
part2() 
part3()

# 21868 wrong, too high






