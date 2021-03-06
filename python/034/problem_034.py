#!/usr/bin/env python


"""
Problem Definition :

145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.

"""

__author__ = 'vivek'

import time
import math


def main():
    start_time = time.clock()

    curious_numbers = []

    for number in xrange(3, 2500000):
        temp = number
        add = 0
        while temp > 0:
            digit = temp % 10
            temp /= 10
            add += math.factorial(digit)
        if number == add:
            curious_numbers.append(number)

    print(curious_numbers)
    print(sum(curious_numbers))

    print "Run time...{} secs \n".format(round(time.clock() - start_time, 4))

if __name__ == '__main__':
    main()


