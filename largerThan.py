#!/usr/bin/env python3

if __name__ == '__main__':
    x = int(input("enter a number: "))
    y = int(input("enter a number: "))
    if x > y:
        print("the value", x , "is greater than the value", y)
    elif x < y:
        print("the value", y, "is greater than", x)
    else:
        print("both values are equal")
