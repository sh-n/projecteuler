#!/usr/bin/env python
# coding=utf-8


"""
Problem Definition :

Triangle, pentagonal, and hexagonal numbers are generated by the following formulae:

Triangle	 	Tn=n(n+1)/2	 	1, 3, 6, 10, 15, ...
Pentagonal	 	Pn=n(3n−1)/2	 	1, 5, 12, 22, 35, ...
Hexagonal	 	Hn=n(2n−1)	 	1, 6, 15, 28, 45, ...
It can be verified that T285 = P165 = H143 = 40755.

Find the next triangle number that is also pentagonal and hexagonal.

"""

__author__ = 'vivek'

import time

startTime = time.clock()

triangle_numbers = [n*(n+1)/2 for n in xrange(1,100000)]
pentagonal_numbers = [n*(3*n-1)/2 for n in xrange(1,100000)]
hexagonal_numbers = [n*(2*n-1) for n in xrange(1,100000)]

print list(set(list(set(hexagonal_numbers).intersection(pentagonal_numbers))).intersection(triangle_numbers))[2]

print "Run time...{} secs \n".format(round(time.clock() - startTime, 4))