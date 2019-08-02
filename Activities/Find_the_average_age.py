numberList = [3, 5, 7, 9, 10]

#add all numbers together
#find number of ages
#divide sum by number of ages

for age in numberList:
    print (age)

print ("Here's the length of our list", len(numberList))

SumOfAges = 0

for i in range(len(numberList)):
    SumOfAges += numberList[i]
#this is how you find the sum of a list!

print ("Here's the sum", SumOfAges)

average = SumOfAges/len(numberList)

print ("Average age is", average)

