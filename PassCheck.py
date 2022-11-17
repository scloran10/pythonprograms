#!/usr/bin/env python3

if __name__ == '__main__':
    passSet = False
    BAD_PASSWORDS = ['password', 'letmein', 'sesame', 'hello', 'justinbieber']
    while passSet == False:
        pass1 = input("Enter your new password: ")
        pass2 = input("Re-enter your new password: ")
        for x in range (0,len(BAD_PASSWORDS)):
            if pass1 != BAD_PASSWORDS[x]:
                if len(pass1) >= 8 and len(pass1) <= 12:
                    if pass1 == pass2:
                        print("Password Set")
                        passSet = True
                        break
                    else:
                        print("Passwords do not match")
                        break
                else:
                    print("Password must be between 8 and 12 characters")
                    break
            else:
                print("Cannot be from the bad password list")
                break
