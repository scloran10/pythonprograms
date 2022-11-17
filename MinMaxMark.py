#!/usr/bin/env python3
from statistics import mean

if __name__ == '__main__':
    mark_1 = int(input('please enter mark #1: '))
    mark_2 = int(input('please enter mark #2: '))
    mark_3 = int(input('please enter mark #3: '))
    mark_4 = int(input('please enter mark #4: '))
    mark_5 = int(input('please enter mark #5: '))
    max_mark = max(mark_1, mark_2, mark_3, mark_4, mark_5)
    min_mark = min(mark_1, mark_2, mark_3, mark_4, mark_5)
    mean_mark = mean([mark_1, mark_2, mark_3, mark_4, mark_5])
    range_mark = (max_mark - min_mark)

    print('highest mark is:', max_mark, '\nlowest mark is:', min_mark, '\nmean mark is:', mean_mark, '\nrange is:', range_mark)