#!/usr/bin/env python3
if __name__ == '__main__':

    def upperCase(string):
        return string.capitalize()
    name = str(input('Hello, what is your name? '))
    if name == "":
        print("Hello, Stranger!")
    else:
        print('Hello,', upperCase(name), '. Good to meet you!')
