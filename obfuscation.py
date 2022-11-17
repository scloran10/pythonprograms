#!/usr/bin/env python3

if __name__ == '__main__':

    def obfuscation(string):
        string = string.replace(" ", "")
        return string[::-1]