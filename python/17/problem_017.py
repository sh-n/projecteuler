#!/usr/bin/env python


#description
#If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
#If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
#NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.

ones = ['','One','Two','Three','Four','Five','Six','Seven','Eight','Nine']
double = ['Ten','Eleven','Twelve','Thirteen','Fourteen','Fifteen','Sixteen','Seventeen','Eighteen','Nineteen']
tens = ['','','Twenty','Thirty','Forty','Fifty','Sixty','Seventy','Eighty','Ninety']
hundreds = ['','','','Hundred','Thousand']

words = 0

for num in xrange(1,1001) :

    word = ''
    
    if len(str(num)) == 4 :
        digit = int(num/1000)
        word = word + ones[digit] + hundreds[4]
        num = num%1000
    
    if len(str(num)) == 3 :
        digit = int(num/100)
        word = word + ones[digit] + hundreds[3]
        num = num%100

        if num <> 0 :
            word = word + 'And'
    
    if len(str(num)) == 2 :
        digit = int(num/10)
        
        if(digit == 1):
            num = num%10
            word = word + double[num]
            num = 0
        else :
            word = word + tens[digit]
            num = num%10
    
    if len(str(num)) == 1 :
        word = word + ones[num]
    
    words = words + len(word)

print words