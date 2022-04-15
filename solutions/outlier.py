def find_outlier(numbers: int):
    if len(numbers) == 0:
        return None
    odd_numbers = []
    even_numbers = []
    
    for number in numbers:
        if number % 2 == 1:
           odd_numbers.append(number)
        else:
            even_numbers.append(number)
    if len(odd_numbers) == 1: 
        return odd_numbers[0]
   
    return even_numbers[0]

    
