# Program with methods related to primes

import math
import sys

# Find the first 'x' k-amlmost prime numbers and return it as a list
def almost_prime(k, x):
    num = 0
    counter = 2
    almost_prime_list = []
    
    while(num < x):
        if (len(prime_decomp(counter)) == k):
            num = num + 1
            almost_prime_list.append(counter)
        counter = counter + 1

    return almost_prime_list

# Determines if a number is prime
# optimize?
def is_prime(number):
    if ((number % 2 == 0) and (number != 2)) or (number <= 1):
        return False
    else:
        # possible use of while loop instead
        for i in range(3, int(math.sqrt(number)) + 1):
            if (number % i == 0):
                return False
    return True

# Returns a list of the prime factors of a number    
def prime_decomp(number):

    if is_prime(number):
        return list([int(number)])
    else:
        for i in range(2, int(math.sqrt(number)) + 1):
            if (number % i == 0):
                return list([int(i)]) + prime_decomp(number / i)

# Determines if a number is an attractive number
# A number is an attractive number if the number of its prime factors
# (whether distinct or not) is also prime
def is_attractive_number(number):
    if(is_prime(len(prime_decomp(number)))):
        return True
    else:
        return False

# Generates a list of the factors of a number
def factors(number):

    factor_list = []
    
    for i in range(1, int(math.sqrt(number)) + 1):
        if (number % i == 0):
            factor_list.append(i)
            if (i**2 != number):
                factor_list.append(number // i)

    return factor_list;

# Generates a list of the factors of a number (in order)
def factors_seq(number):
    factor_list = []

    for i in range(1, number + 1):
        if (number % i == 0):
            factor_list.append(i)

    return factor_list

# Determines if a number is an anti-prime
def is_anti_prime(number):

    num_factors = len(factors_seq(number))

    for i in range(1, num_factors):
        if len(factors_seq(number - i)) >= num_factors:
            return False

    return True

# Generates a list if the first 'numInlist' anti-prime numbers (highly composite number)
def anti_prime_list(num_ln_list):

    num_anti_primes = 0
    largest_num_factors = 0
    number = 1
    anti_prime_list = []

    while (num_anti_primes < num_in_list):

        factor_size = len(factors_seq(number))

        if (factor_size > largest_num_factors):
            anti_prime_list.append(number)
            largest_num_factors = factor_size
            num_anti_primes = num_anti_primes + 1

        number = number + 1

    return anti_prime_list

def main ():

    # Tests / Output
    number = int(sys.argv[1])
    k = 1
    num_almost_prime = 1
    
    print("Number:", number)
    print("Prime Decompositon of", str(number) + ":", * prime_decomp(number))
    print("Attractive Number?:", is_attractive_number(number))
    print("List of factors:", * factors_seq(number))
    print("Is anti-prime?:", is_anti_prime(number))

    #print(*antiPrimeList(20))

    print()
    print(str(k) + "-almost primes:", *almost_prime(k, num_almost_prime))

main()
