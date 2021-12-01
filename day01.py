def part1() : 

    with open("input/day01.txt") as file : 

        previousMeasurement = 0
        increaseCounter = 0

        for line in file : 
            
            currentMeasurement = int(line)

            if (currentMeasurement > previousMeasurement) : 
                increaseCounter += 1
            previousMeasurement = currentMeasurement
    
    print(increaseCounter - 1)

def part2() : 

    with open("input/day01.txt") as file : 

        windowStack = []
        previousMeasurement = 0
        depthIncreaseCounter = 0 

        for line in file : 

            currentMeasurement = int(line.strip())

            if len(windowStack) < 3 : 
                windowStack.append(currentMeasurement)

            if len(windowStack) == 3 :
                if sum(windowStack) > previousMeasurement :  
                    depthIncreaseCounter += 1
                previousMeasurement = sum(windowStack)
                windowStack.pop(0)


        print(depthIncreaseCounter - 1)
            

part1()  
part2()