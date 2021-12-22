import random 

minimumDifference = 1000
minimumI = 0
numberOfTries = []

for i in range (10000) :

    count = 0 
    partialSum = 0 

    while partialSum < 1 : 

        number = random.random()
        partialSum += number
        count += 1
    
    numberOfTries.append(count)

    average = sum(numberOfTries) / len(numberOfTries)

    difference = abs(average - 2.7182818)

    if difference < minimumDifference : 
        minimumDifference = difference
        minimumI = i



    print(average, difference)

print(minimumDifference, i)

