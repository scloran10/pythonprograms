#!/usr/bin/env python3

if __name__ == '__main__':

    def removeLastChar(string):
        return string[:-1]
    cent = int(removeLastChar(input("enter centegrade value followed by letter C: ")))
    print(((cent * 9/5) + 32), "F")
