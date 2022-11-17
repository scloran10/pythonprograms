#!/usr/bin/env python3
if __name__ == '__main__':
    students = int(input('How many students? '))
    group_size = int(input('Group size? '))
    print(str('There will be ' + str(int(students // group_size)) + ' groups with ' + str(int(students % group_size)) + (' students leftover')))
