def part1() : 
    
    test = False
    length = 5 if test else 12

    with open("input/day03.txt") as file : 

        count0 = [0] * length
        count1 = [0] * length

        for line in file : 

            position = 0
            for character in line.rstrip() : 
                if character == "0" : 
                    count0[position] += 1
                else : 
                    count1[position] += 1
                position +=1
            
        print(count0 , count1)

        gamaRate = []
        epsilonRate = []
        for i in range(length) : 
            if count0[i] > count1[i] : 
                gamaRate.append("0")
                epsilonRate.append("1")
            else : 
                gamaRate.append("1")
                epsilonRate.append("0")

        decimalNumberGama = int("".join(gamaRate),2)
        decimalNumberEpsilon = int("".join(epsilonRate),2)

        print(decimalNumberGama * decimalNumberEpsilon) 

def part2() : 
    
    lines = []

    with open("input/day03.txt") as file : 

        for line in file : 
            lines.append(line.rstrip())  

    recursiveThinningOut(lines, 0, "common")
    recursiveThinningOut(lines, 0, "rarest")

    print(2815 * 1059)

def recursiveThinningOut(lines, depth, option) : 

    # Step 1 : Find which is the most common depth-st character.
    depthBits = []
    for line in lines : 

        depthBits.append(line[depth])

    # Step 2: Count which is the most common/rare one : 
    if option == "common" : 
        selectedCharacter = "0" if depthBits.count("0") > depthBits.count("1") else "1"
    else : 
        # Option is rarest : 
        selectedCharacter = "1" if depthBits.count("0") > depthBits.count("1") else "0"

    # Step 3 : Thin out the lines 
    thinnedOutLines = []

    for line in lines : 
        if line[depth] == selectedCharacter : 
            thinnedOutLines.append(line)
        
    if (len(thinnedOutLines) != 1 ) : 
        recursiveThinningOut(thinnedOutLines, depth + 1, option)
    else : 
        print("Rating : ", int("".join(thinnedOutLines),2))
        return int("".join(thinnedOutLines),2)

part1()
part2() 