
def to_hex(number: int):
    if number <= 0:
        return "00"
    elif number < 10:
        return f"0{number}"
    elif number > 255:
        return "FF"

    result = hex(number).replace("0x", "").upper()

    if len(result) == 1:
        return result * 2
    return result

def rgb(red, green, blue):
    return to_hex(red) + to_hex(green) + to_hex(blue)
