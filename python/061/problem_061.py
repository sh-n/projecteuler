#!/usr/bin/env python
# coding=utf-8


"""
Problem Definition :

Triangle, square, pentagonal, hexagonal, heptagonal, and octagonal numbers are all figurate (polygonal) numbers and are generated by the following formulae:

Triangle	 	P3,n=n(n+1)/2	 	1, 3, 6, 10, 15, ...
Square	 	P4,n=n2	 	1, 4, 9, 16, 25, ...
Pentagonal	 	P5,n=n(3n−1)/2	 	1, 5, 12, 22, 35, ...
Hexagonal	 	P6,n=n(2n−1)	 	1, 6, 15, 28, 45, ...
Heptagonal	 	P7,n=n(5n−3)/2	 	1, 7, 18, 34, 55, ...
Octagonal	 	P8,n=n(3n−2)	 	1, 8, 21, 40, 65, ...
The ordered set of three 4-digit numbers: 8128, 2882, 8281, has three interesting properties.

The set is cyclic, in that the last two digits of each number is the first two digits of the next number (including the last number with the first).
Each polygonal type: triangle (P3,127=8128), square (P4,91=8281), and pentagonal (P5,44=2882), is represented by a different number in the set.
This is the only set of 4-digit numbers with this property.
Find the sum of the only ordered set of six cyclic 4-digit numbers for which each polygonal type: triangle, square, pentagonal, hexagonal, heptagonal, and octagonal, is represented by a different number in the set.
"""

__author__ = 'vivek'

import time


def triangle(num):
    return num*(num+1)/2


def square(num):
    return num*num


def pentagonal(num):
    return num*(3*num - 1)/2


def hexagonal(num):
    return num*(2*num - 1)


def heptagonal(num):
    return num*(5*num - 3)/2


def octagonal(num):
    return num*(3*num - 2)


def main():

    startTime = time.clock()

    tri = []
    squa = []
    penta = []
    hexa = []
    hepta = []
    octa = []

    all_numbers = []

    answer = 0
    number = 1
    while answer < 10000:
        answer = triangle(number)
        if answer > 999:
            tri.append(answer)
        number += 1

    answer = 0
    number = 1
    while answer < 10000:
        answer = square(number)
        if answer > 999:
            squa.append(answer)
        number += 1

    answer = 0
    number = 1
    while answer < 10000:
        answer = pentagonal(number)
        if 999 < answer < 10000:
            penta.append(answer)
        number += 1

    answer = 0
    number = 1
    while answer < 10000:
        answer = hexagonal(number)
        if 999 < answer < 10000:
            hexa.append(answer)
        number += 1

    answer = 0
    number = 1
    while answer < 10000:
        answer = heptagonal(number)
        if 999 < answer < 10000:
            hepta.append(answer)
        number += 1

    answer = 0
    number = 1
    while answer < 10000:
        answer = octagonal(number)
        if 999 < answer < 10000:
            octa.append(answer)
        number += 1

    all_numbers.append(tri)
    all_numbers.append(squa)
    all_numbers.append(penta)
    all_numbers.append(hexa)
    all_numbers.append(hepta)
    all_numbers.append(octa)

    sets1 = []
    sets2 = []

    for i in xrange(6):
        for j in xrange(6):
            sets1 = []
            if i != j:
                for num1 in all_numbers[i]:
                    for num2 in all_numbers[j]:
                        if str(num1)[-2:] == str(num2)[:2]:
                            sets1.append((num1, num2))

            for k in xrange(6):
                sets2 = []
                if i != k and j != k:
                    for num1 in all_numbers[k]:
                        for num2 in sets1:
                            if str(num1)[-2:] == str(num2[0])[:2]:
                                sets2.append((num1, num2[0], num2[1]))

                for l in xrange(6):
                    sets3 = []
                    if i != l and j != l and k != l:
                        for num1 in all_numbers[l]:
                            for num2 in sets2:
                                if str(num1)[-2:] == str(num2[0])[:2]:
                                    sets3.append((num1, num2[0], num2[1], num2[2]))

                    for m in xrange(6):
                        sets4 = []
                        if i != m and j != m and k != m and l != m:
                            for num1 in all_numbers[m]:
                                for num2 in sets3:
                                    if str(num1)[-2:] == str(num2[0])[:2]:
                                        sets4.append((num1, num2[0], num2[1], num2[2], num2[3]))

                        for n in xrange(6):
                            sets5 = []
                            if i != n and j != n and k != n and l != n and m != n:
                                for num1 in all_numbers[n]:
                                    for num2 in sets4:
                                        if str(num1)[-2:] == str(num2[0])[:2] and str(num1)[:2] == str(num2[4])[-2:]:
                                            sets5.append((num1, num2[0], num2[1], num2[2], num2[3], num2[4]))
                            if sets5:
                                print(sets5)
                                break
                        if sets5:
                            break
                    if sets5:
                        break
                if sets5:
                    break
            if sets5:
                break
        if sets5:
            break

    print(sum(sets5[0]))

    print "Run time...{} secs \n".format(round(time.clock() - startTime, 4))


if __name__ == '__main__':
    main()

