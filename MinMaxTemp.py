#!/usr/bin/env python3
from statistics import mean

if __name__ == '__main__':
    temp_1 = int(input('please enter temperature #1 in celcius: '))
    temp_2 = int(input('please enter temperature #2 in celcius: '))
    temp_3 = int(input('please enter temperature #3 in celcius: '))
    temp_4 = int(input('please enter temperature #4 in celcius: '))
    temp_5 = int(input('please enter temperature #5 in celcius: '))
    max_temp = max(temp_1, temp_2, temp_3, temp_4, temp_5)
    min_temp = min(temp_1, temp_2, temp_3, temp_4, temp_5)
    mean_temp_c = mean([temp_1, temp_2, temp_3, temp_4, temp_5])
    mean_temp_f = mean([((temp_1 * 9/5) + 32), ((temp_2 * 9/5) + 32), ((temp_3 * 9/5) + 32), ((temp_4 * 9/5) + 32), ((temp_5 * 9/5) + 32)])
    range_mark_c = (max_temp - min_temp)
    range_mark_f = ((max_temp * 9/5) + 32)-((min_temp * 9/5) + 32)

    print()
    print('in celcius:\nhighest temperature is:', max_temp, '\nlowest temperature is:', min_temp, '\nmean temperature is:', mean_temp_c, '\nrange is:', range_mark_c)
    print()
    print('in fahrenheit:\nhighest temperature is:', ((max_temp * 9/5) + 32), '\nlowest temperature is:', ((min_temp * 9/5) + 32),
          '\nmean temperature is:', mean_temp_f, '\nrange is:', range_mark_f)