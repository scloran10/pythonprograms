#!/usr/bin/env python3
if __name__ == '__main__':
    pupils = int(input('How many pupils in class? '))
    sweets = int(input('How many sweets in tub? '))
    print((str('Each student gets ' + str(int(sweets // pupils)) + ' sweets, with ' + str(
        int(sweets % pupils)) + ' leftover')))
