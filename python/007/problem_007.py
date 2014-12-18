#!/usr/bin/env python

"""
Problem Definition :

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10001st prime number?

"""

import math

def isPrime(number) :
    if number == 2 or number == 3 :
        return 1
    elif number % 2 == 0 or number % 3 ==0 or number == 1 :
        return 0
    else :
        start = 5   
        while (start <= int(math.sqrt(number))) :
        
            if(number % start == 0) :
               return 0
               break
            if(number % (start+2) == 0) :
               return 0
               break
            start = start + 6
        return 1 


num = 1
count = 1

while count < 10001 :
    num = num + 2
    if isPrime(num) :
        count = count + 1

print num