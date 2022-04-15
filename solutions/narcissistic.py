import math
def is_narcissistic(number):
    temp_number = number
    number_of_digits = int(math.log10(number)) + 1
    total = 0
    while number > 0:
        digit = number % 10
        total += digit ** number_of_digits
        number = number // 10
    
    return total == temp_number
    
    

    