#!/usr/bin/env python3

if __name__ == '__main__':
    spamCount = 0
    spamString = "Spam"
    outputString = "Spam"
    while spamCount == 0:
        spamCount = int(input("How many slices of spam? "))
        if spamCount == 0:
            print("Must have at least 1 slice")
        else:
            for x in range(spamCount-1):
                if x == 1:
                    outputString = outputString + " and Spam"
                else:
                    outputString = outputString + ", Spam"
            print("Eggs with", outputString, "coming up!")