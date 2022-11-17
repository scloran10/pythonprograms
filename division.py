#!/usr/bin/env python3

if __name__ == '__main__':
    x = int(input("enter a number: "))
    y = int(input("enter a number: "))
    if y == 0:
        print("division by 0 is not possible")
    else:
        print(int(x/y))