# Algorithm to compute the principal nth root of a positive real number
#   using Newton's method

from decimal import *
import sys

# Method to compute the principal nth root of a number
#   iterations: number of iteratins using Newton's method
#   number    : number who's
def nth_root (number, root, iterations):

    starting_base = get_base(number, root)
    base = nth_root_helper(iterations, starting_base, root, number)
    return base
    
# Method to get a close base value for the nth root
#   number: your number
#   root  : nth root    
def get_base (number, root):

    #begin with base 2
    base = Decimal(2)
    
    # iterate to find a base where base^root is closest to,
    #   but not over number
    while ((base + 1) ** root) < number:
        base = base + 1

    return base

# Helper method to recursively find the nth root of a number
#   iterations: number of iterations using Newton's method
#   x         : base
#   n         : root
#   number    : your number
def nth_root_helper (iterations, x, n, number):

    iterations = iterations - 1
    
    # base case, return your base
    if (iterations == 0):
        return x
    
    # Newton's method calculation
    expr1 = Decimal(1) / n
    expr2 = (n - Decimal(1)) * x
    expr3 = number / (x ** (n - Decimal(1)))
    
    new_base = expr1 * (expr2 + expr3)
    
    # Recursive call
    return nth_root_helper(iterations, new_base, n, number)

# main method
# command line arguments
# "python newtons_method.py [x] [y] [z]"
#   x: your number
#   y: nth root
#   z: iterations (50 will be used if left empty)
def main():
    
    number = Decimal(sys.argv[1])
    root = Decimal(sys.argv[2])

    if (len(sys.argv) < 4):
        iterations = 50
    else:
        iterations = Decimal(sys.argv[3])

    # Example, using 10 iterations, a number of 100, and 5th root
    print("Base:", nth_root(number, root, iterations))

# Begin
main()
    