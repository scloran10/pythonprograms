#!/usr/bin/env python3

if __name__ == '__main__':
    tableNum = int(input("enter a number: "))
    if tableNum >= 0:
        for x in range(0, 13):
            print(x, "x", tableNum, "=", x * tableNum)
    else:
        y = 12
        while y>=0:
            print(y, "x", tableNum, "=", y * tableNum)
            y -= 1