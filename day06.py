
'''
Each day : 
- A 0 becomes a 6, and also add an 8 to the end of the list.
- Everything else just decreases by 1
'''

def passingDay(laternfish : list) :
    for i in range(len(laternfish)) : 

        if laternfish[i] == 0 : 
            
            laternfish[i] = 6
            laternfish.append(8)
        else : 
            laternfish[i] -= 1

def fastPassingDay(counts : dict) : 

    newCounts = dict.fromkeys([i for i in range(9)], 0)
    for i in range(0,8) :
        newCounts[i] = counts[i+1]

    newCounts[6] += counts[0]
    newCounts[8] += counts[0]

    return newCounts

    
def part1() : 
    with open("input/day06.txt") as file : 
            
            for line in file : 
                lanternFish = [int(i) for i in line.rstrip().split(",")]

                for i in range(80) : 

                    passingDay(lanternFish) 
                
                print(len(lanternFish))

'''
We just need to count the number of fish for each day : 
'''

def part2(days) : 

    # We can't do the same for 256 LMAO
    with open("input/day06.txt") as file : 
            
        for line in file : 
            lanternFish = [int(i) for i in line.rstrip().split(",")]

            # Initialize first dict 
            counts = dict.fromkeys([i for i in range(9)], 0)
            for fish in lanternFish : 
                counts[fish] +=1


            for i in range(days) : 
                counts = fastPassingDay(counts)
            
            print(sum(counts.values()))

# part1()
part2(80)
part2(256)