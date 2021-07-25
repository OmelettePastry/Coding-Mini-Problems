# This program outputs gapful numbers

from decimal import *
import sys

# This method determines if a number is a gapful number
def is_gapful(number):
    
    # boolean for our number
    gapful = False;

    divisor = Decimal(10)
    
    while (number > (divisor * Decimal(10))):
        divisor = divisor * Decimal(10)

    # first digit of our number, in tens place
    first_digit = (number // divisor) * Decimal(10)
    
    # last digit
    last_digit = number % Decimal(10)
   
    # our divisor for our number
    gapful_divisor = first_digit + last_digit
    
    # Determine if our number is a gapful number
    if (number % gapful_divisor == Decimal(0)):
        gapful = True
        
    return gapful

# main method    
# Our program outputs the gapful numbers between 100 and maxNumber
def main():

    max_number = 1000
    
    # output the gapful numbers between 100 and maxNumber
    for x in range(100, max_number + 1):
        if is_gapful(Decimal(x)):
            print(x, end = ", ")    
    
main()