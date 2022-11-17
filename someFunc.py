#!/usr/bin/env python3

if __name__ == '__main__':

    def someFunc(x,y,z):
        print("x is", x, "\ny is", y, "\nz is", z)

    someFunc(1,2,3)
    someFunc(y=2,x=1,z=3)
    someFunc(1,z=99,y=4)