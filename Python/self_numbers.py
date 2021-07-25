# This program has functions related to self numbers# 
# A number n is a self number if there is no number g such that g + the sum of g's digits = n

# This function generates a list of the first 'n' self numbers
def self_number_list(n):
    
    self_number_counter = 1
    iter_counter = 0
    self_number_list = []
    
    while (self_number_counter != n):
        iter_counter = iter_counter + 1
        if is_self_number(iter_counter):
            self_number_counter = self_number_counter + 1
            self_number_list.append(iter_counter)
            
    return self_number_list

# This function generates the npth self number
def nth_self_number(n):
    
    self_number_counter = 1
    iter_counter = 0
    
    while (self_number_counter != n):
        iter_counter = iter_counter + 1
        if is_self_number(iter_counter):
            self_number_counter = self_number_counter + 1
            
    return iter_counter

# This funtion determines if a nunber is a self number
def is_self_number(number):
    
    self_number = True
    counter = 1
    
    divisor = 0
    digits = 1
 
    while (self_number != False) and (counter <= number):
        g = number - counter
        if(g + digit_sum(g)) == number:
            self_number = False

        counter = counter + 1
        
    return self_number

# This funtion determines if a nunber is a self number
# This function is a somewhat more efficient self number function, as it doesn't test all
#   the numbers less than 'number'. The algorithm calculates a minimum value of g
def is_self_number_opt(number):
    
    self_number = True
    counter = 1
    
    divisor = 0
    digits = 1
    
    while ((divisor * 10 ) < number):
        if (divisor != 0):
            divisor = divisor * 10
        else:
            divisor = 10
        digits = digits + 1
        
    min_number = number - ((9 * (digits - 1)) + ((number // divisor) - 1))
    print(digits)
    print(number // divisor - 1)
    print(min_number)
    
    while (self_number != False) and (counter <= (number - min_number)):
        g = number - counter
        if(g + digit_sum(g)) == number:
            self_number = False
            
        print(counter)
        counter = counter + 1
        
    return self_number

# This function calculates the sum of a number's digits
def digit_sum(number):
    digit_sum = 0
    base_10_exp = 0
    divisor = 0
    
    while (divisor < number):
        base_10_exp = base_10_exp + 1
        divisor = 10 ** base_10_exp
        divisor_lower = 10 ** (base_10_exp - 1)
        digit_sum = digit_sum + ((number % divisor) // (divisor_lower))
        
    return digit_sum

# main
def main():
    print(is_self_number(1016))
    print(nth_self_number(10))
    print(*self_number_list(50))

main()