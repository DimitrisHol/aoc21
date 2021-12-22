'''
You must find a position, which they can all horizontally align
and that's it's gonna require the least fuel to do so (in total)
'''
def part1() : 
    with open("input/day07.txt") as file : 

        for line in file : 

            # Step 1 : Get a list with all the positions. 
            positions = [int(i) for i in line.rstrip().split(",")]

            # Step 2 : Get a count for the crabs for each position 
            counts = {}
            # Count how many times each number is found 
            for i in range(len(positions)) : 
                counts[positions[i]] = positions.count(positions[i])

            print(positions)
            print(counts)

            fuelRequirements = [1000000000000, None]

            for i in range(min(positions), max(positions) + 1) : 
                fuelRequired = 0

                # Calculate the distance for each position
                # i = 0 , how much fuel to transfer everyone to 0

                for key in counts.keys() : 
                    distance = abs(i - key) # 
                    part2Consumption = sum([i for i in range(distance+1)])

                    fuelRequired += distance * counts[key] # Part 1
                    fuelRequired += part2Consumption * counts[key]  # Part 2 , kinda slow
                
                if fuelRequired < fuelRequirements[0] : 
                    fuelRequirements[0] = fuelRequired
                    fuelRequirements[1] = i

            print(fuelRequirements)

part1()