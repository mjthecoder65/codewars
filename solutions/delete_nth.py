def delete_nth(order: list, max_e: int):
    result = []
    counter = {}

    for item in order:
        if item not in counter:
            result.append(item)
            counter[item] = 1
        else:
            if counter[item] < max_e:
                result.append(item)
                counter[item] += 1

    return result