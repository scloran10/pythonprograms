#!/usr/bin/env python3
import statistics
from statistics import mean
if __name__ == '__main__':

    def removeLastChar(string):
        return string[:-1]
    def calcMean(a,b,c,d,e,f):
        return mean([a,b,c,d,e,f])
    def calcMax(a,b,c,d,e,f):
        return max(a,b,c,d,e,f)
    def calcMin(a,b,c,d,e,f):
        return min(a,b,c,d,e,f)

    print("Enter all values in the format 50C:")
    temp_1 = int(removeLastChar(input('please enter temp #1: ')))
    temp_2 = int(removeLastChar(input('please enter temp #2: ')))
    temp_3 = int(removeLastChar(input('please enter temp #3: ')))
    temp_4 = int(removeLastChar(input('please enter temp #4: ')))
    temp_5 = int(removeLastChar(input('please enter temp #5: ')))
    temp_6 = int(removeLastChar(input('please enter temp #6: ')))
    print("Max temp is: ", calcMax(temp_6, temp_5, temp_4, temp_3, temp_2, temp_1))
    print("Min temp is: ", calcMin(temp_6, temp_5, temp_4, temp_3, temp_2, temp_1))
    print("Mean temp is: ", calcMean(temp_6, temp_5, temp_4, temp_3, temp_2, temp_1))

