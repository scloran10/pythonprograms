#!/usr/bin/env python3

if __name__ == '__main__':

    def validate(a):
        if (0 <= a <= 100):
            return True
        else:
            return False
    print(validate(5))