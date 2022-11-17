#!/usr/bin/env python3

if __name__ == '__main__':

    def findMax(a,b):
        """Finds maximum of two values."""
        if(a>b):
            max = a
        else:
            max = b
        return max

    print(findMax(78,98))