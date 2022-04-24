def solution(args: list) -> str:
    result = []
    temp = []
    for item in args:
        if len(temp) == 0:
            temp.append(item)
        else:
            diff = item - temp[-1]
            if diff == 1:
                temp.append(item)
            else:
                result.append(temp)
                temp = [item]
    
    result.append(temp)

    outputs = []
    for item in result:
        if len(item) >= 3:
            start = item[0]
            end = item[-1]
            interval = f"{start}-{end}"
            outputs.append(interval)
        elif len(item) == 1:
            outputs.append(str(item[0]))
        else:
            outputs.append(str(item[0]))
            outputs.append(str(item[1]))

    return ",".join(outputs)


if __name__ == "__main__":
    res = solution([-6,-3,-2,-1,0,1,3,4,5,7,8,9,10,11,14,15,17,18,19,20])
    print(res)



    

