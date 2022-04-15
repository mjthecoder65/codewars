def digital_root(number):
    if number < 10:
        return number
    total = 0
    while number > 0:
        digit = number % 10
        number = number // 10
        total += digit
    return digital_root(total)

        