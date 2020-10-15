#find number of ages
#divide sum by number of ages

for age in numberList:
    print (age)

print ("Here's the length of our list", len(numberList))

SumOfAges = 0

for i in range(len(numberList)):
    SumOfAges += numberList[i]
for i in numberList:
    SumOfAges += i
#this is how you find the sum of a list!

print ("Here's the sum", SumOfAges)
