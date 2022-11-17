#!/usr/bin/env python3

if __name__ == '__main__':
    def factors(int):
        for i in range(1, int + 1):
            if int % i == 0:
                print(i)
    factors(1024)
