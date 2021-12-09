arraySize = 1000

def part1() : 

    # ventArray = [[0] * arraySize] * arraySize don't use this lol it's reference
    ventArray = [ [0] * arraySize for i in range(arraySize)]

    with open("input/day05.txt") as file : 
        

        for line in file : 
            inputLine = line.rstrip().split(" -> ")

            startingValue = inputLine[0].split(",")
            finalValue = inputLine[1].split(",")


            if int(startingValue[0]) < int(finalValue[0]) : 
                x1 = int(startingValue[0])
                x2 = int(finalValue[0])
            else : 
                x2 = int(startingValue[0])
                x1 = int(finalValue[0])

            if (int(startingValue[1]) < int(finalValue[1])) : 
                y1 = int(startingValue[1])
                y2 = int(finalValue[1])
            else : 
                y2 = int(startingValue[1])
                y1 = int(finalValue[1])

            if y1 == y2 : 
                for i in range(x1,x2+1) : 
                    ventArray[y1][i] += 1
            elif x1 == x2 : 
                for i in range(y1,y2+1) : 
                    ventArray[i][x1] += 1

        count = 0
        for line in ventArray : 
            for number in line : 
                if number >= 2 : 
                    count +=1

        print(count)
part1()

