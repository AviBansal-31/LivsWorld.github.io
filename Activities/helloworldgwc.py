#prints hello world
print("Hello, world")

answer = input("Who inspires you?")
print(answer, "inspires you!")

i=0
while i<5:
    print(i)
    i+=1
    #i=i+1
    
for i in range(5):
    print(i)

i=-1
while True:
    i+=1
    if(i>20):
        break
    #i is odd
    if(i%2!=0):
        continue
    print(i)
