#!/usr/bin/env python3

if __name__ == '__main__':

    def calcAve(*numbers):
        total=0
        for num in numbers:
            total += num
        return total/len(numbers)

    print(calcAve(2,4,6,8))