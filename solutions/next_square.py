import math

# def find_next_square(sq):
#     square = math.sqrt(sq)

#     if square != int(square):
#         return -1

#     return (square + 1) ** 2


def find_next_square(sq):
    square = sq ** 0.5

    if square.is_integer():
        return (square + 1) ** 2

    return -1
