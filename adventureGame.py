#!/usr/bin/env python3

if __name__ == '__main__':
    nameCorrect = False
    while nameCorrect == False:
        inputName = str(input("Greetings! How shall we call you? "))
        firstFourChar = inputName[0: 4]
        if firstFourChar != "Lord" and firstFourChar != "Lady":
            print("You may not be known by that name!")
        else:
            print("It shall be so,", inputName)
            nameCorrect = True

