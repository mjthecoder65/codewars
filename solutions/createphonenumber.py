
def create_phone_number(numbers):
    numbers = [str(number) for number in numbers]
    first_part = ''.join(numbers[0:3])
    second_part = ''.join(numbers[3:6])
    last_part = ''.join(numbers[6:])

    return f"({first_part}) {second_part}-{last_part}"

# Another solution
def create_phone_number(n):
    return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)