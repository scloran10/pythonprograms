#!/usr/bin/env python3

if __name__ == '__main__':

    def isPrime(x):
        for i in range(2,x):
            if (x % i) == 0:
                return False
        return True

    print(isPrime(22))