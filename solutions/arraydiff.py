# def array_diff(a, b):
#     if len(b) == 0:
#         return a
#     diff = []
#     for number in a:
#         if number not in b:
#             diff.append(number)
#     return diff


def array_diff(a, b):
    if len(b) == 0: return a
    checkpoint = set(b)
    return [number for number in a if number not in checkpoint]


__all__ = ['array_diff']