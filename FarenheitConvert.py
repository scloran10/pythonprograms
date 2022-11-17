#!/usr/bin/env python3

if __name__ == '__main__':

    def FtoC(a):
        return (a - 32) * 5/9
    def CtoF(b):
        return (b * 9/5) + 32
    print("Farenheit to Celcius:", FtoC(50))
    print("Celcius to Farenheit:", CtoF(21))

