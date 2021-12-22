'''
You must find a position, which they can all horizontally align
and that's it's gonna require the least int(fuel) to do so (in total)
'''
def solve() : 
    with open("input/day07.txt") as file : 

        for line in file : 

            # Step 1 : Get a list with all the positions. 
            positions = [int(i) for i in line.rstrip().split(",")]

            # Step 2 : Get a count for the crabs for each position 
            counts = {}
            # Count how many times each number is found 
            for i in range(len(positions)) : 
                counts[positions[i]] = positions.count(positions[i])

            minimumFuelRequiredPart1 = 1000000000000
            minimumFuelRequiredPart2 = 1000000000000

            for i in range(min(positions), max(positions) + 1) : 
                fuelRequiredPart1 = 0
                fuelRequiredPart2 = 0

                # Calculate the distance for each position
                # i = 0 , how much fuel to transfer everyone to 0

                for key in counts.keys() : 
                    distance = abs(i - key) 

                    # part2Consumption = sum([i for i in range(distance+1)])  # This is really really slow 
                    # https://en.wikipedia.org/wiki/Triangular_number
                    
                    # You can calculate it really fast with this : 
                    part2Consumption = (distance * (distance + 1)) / 2

                    fuelRequiredPart1 += distance * counts[key] # Part 1
                    fuelRequiredPart2 += part2Consumption * counts[key]  # Part 2
                
                minimumFuelRequiredPart1 = min(minimumFuelRequiredPart1, fuelRequiredPart1)
                minimumFuelRequiredPart2 = min(minimumFuelRequiredPart2, fuelRequiredPart2)


            print("Part 1 :", minimumFuelRequiredPart1)
            print("Part 2 :", int(minimumFuelRequiredPart2))

solve()