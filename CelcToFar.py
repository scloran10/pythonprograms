#!/usr/bin/env python3
if __name__ == '__main__':
    celcius_value = float(input('Enter a temperature in Celcius: '))
    farenheit_value = str((celcius_value * 9/5) + 32)
    print(str(celcius_value) + 'C is equivalent to', farenheit_value + ('F'))