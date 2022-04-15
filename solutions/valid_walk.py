from collections import Counter, defaultdict

# def is_valid_walk(walk):
#     if len(walk) != 10:
#         return False
#     else:
#         counter = Counter(walk)
#         keys = counter.keys()
#         key_count = len(keys)
#         if key_count % 2 != 0:
#             return False
#         elif key_count == 2:
#             if "n" in counter or "s" in counter:
#                 return counter["n"] == counter["s"]
#             elif "w" in counter or "e" in counter:
#                 return counter["w"] == counter["e"]
#             else:
#                 return False
#         else:
#             return counter["s"] == counter["n"] and counter["w"] == counter["e"]
            


# def is_valid_walk(walk):
#     if len(walk) != 10:
#         return False
#     else:
#         counter = defaultdict(lambda: 0, Counter(walk))
#         return counter['n'] == counter['s'] and counter['w'] == counter["e"]


def is_valid_walk(walk):
    return len(walk) == 10 and walk.count("n") == walk.count("s") \
             and walk.count('e') == walk.count('w')

        