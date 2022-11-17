#!/usr/bin/env python3

if __name__ == '__main__':

    import random
    def encrypt(string):
        interval = random.randint(2,5)
        print(interval)
        for x in range(0,interval):
            string = " ".join(string)
        string = string.replace(" ", "xy")
        print(string)

    encrypt("send cheese")
