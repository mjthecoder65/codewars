def solution(number):
    thousands = ["", "M", "MM", "MMM"]
    hundreds = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
    tens = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
    ones = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
 
    thousands = thousands[number // 1000]
    hundreds = hundreds[(number % 1000) // 100]
    tens = tens[(number % 100) // 10]
    ones = ones[number % 10]
 
    roman_number = thousands + hundreds + tens + ones
 
    return roman_number