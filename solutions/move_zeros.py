# def move_zeros(array):
#     zeros = []
#     res = []

#     for number in array:
#         if number == 0: 
#             zeros.append(number)
#         else:
#             res.append(number)

#     for zero in zeros:
#         res.append(zero)

#     return res

def move_zeros(array):
    zeros = []
    res = []

    for number in array:
        if number == 0: 
            zeros.append(number)
        else:
            res.append(number)

    res.extend(zeros)

    return res
    