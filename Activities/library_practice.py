import math
from turtle import *
#if you put * after the library, it pulls all the features from the library
#this way you don't have to put library name before everything

def main():
    print(math.sqrt(16))
#sqrt returns a float, not and integer
    print(math.floor(1.999))
    print(math.factorial(4))

    color('light blue', 'yellow')
    begin_fill()
    while True:
        forward(100)
        left(170)
        if abs(pos()) < 1:
            break
    end_fill()
    done()

main()
