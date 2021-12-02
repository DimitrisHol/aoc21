def part1() : 

    with open("input/day02.txt") as file : 

        horizontalMovement = 0
        verticalMovement = 0 

        for line in file : 

            move = line.strip().split(" ")
            movement = int(move[1])

            if move[0] == "forward" : 
                horizontalMovement += movement
            elif move[0] == "down" : 
                verticalMovement += movement
            else :
                verticalMovement -= movement
            
        print(horizontalMovement * verticalMovement)
            

def part2() : 

    with open("input/day02.txt") as file : 

        horizontalMovement = 0
        verticalMovement = 0 
        aim = 0

        for line in file : 

            move = line.strip().split(" ")
            movement = int(move[1])

            if move[0] == "forward" : 
                horizontalMovement += movement
                verticalMovement += movement * aim
            elif move[0] == "down" : 
                aim += movement
            else :
                aim -= movement
            
        print(horizontalMovement * verticalMovement)

part1()
part2()