listWomenInTech = ["June", "Rebecca", "Maya", "Amanda", "Tran"]
#for each name in list, print it out
#This will print out each name once
#you can also use a for loop and repeat iteration 5 times

for name in listWomenInTech:
    print (name)
print(len(listWomenInTech))
print("June" in listWomenInTech)

listMixed = [2>3, 7, "banana"]

listCombine = [listWomenInTech, listMixed]
for name in listCombine:
    print (name)

listWomenInTech.append(listMixed)
print (listWomenInTech)
