def open_or_senior(data):
    output = []

    for pair in data:
        if pair[0] >= 55 and pair[1] > 7:
            output.append("Senior")
        else:
            output.append("Open")
            
    return output