#!/usr/bin/env python3

if __name__ == '__main__':
    secretPassword = "parrot"
    passCorrect = False
    while passCorrect == False:
        enteredPass = str(input("Greetings! What is the password? "))
        if enteredPass == secretPassword:
            passCorrect = True
            print("Correct! You may enter.")
        else:
            print("Incorrect! You may try again.")