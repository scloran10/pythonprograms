#!/usr/bin/env python3

if __name__ == '__main__':

    def upperLower(string):
        upper = sum(1 for c in string if c.isupper())
        lower = sum(1 for c in string if c.islower())
        print("Uppercase:", upper, "\nLowercase:", lower)
    upperLower("GFDggfdsGF")