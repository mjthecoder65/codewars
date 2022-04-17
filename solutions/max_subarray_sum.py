

# Helper function
def all_negative(arr):
    """Returns true if all elements in arr are negative"""
    for number in arr:
        if number >= 0:
            return False
    return True


# Brute force solution 
def max_sequence(arr):
    if all_negative(arr):
        return 0
    
    subarrays = []

    for i in range(len(arr)):
        sub_arr = []
        for j in range(i, len(arr)):
            sub_arr.append(arr[j])
            temp = list(sub_arr)
            subarrays.append(temp)
        subarrays.append(sub_arr)

    max_sum = sum(arr)
    for sub in subarrays:
        if sum(sub) > max_sum:
            max_sum = sum(sub)
        
    return max_sum

# Dynamic Programming using Kadane Algorithm: Time complexity O(N) and space complexity O(1)

def max_sequence(arr):
    """Return the sum of subarray that is maximum of all"""
    if all_negative(arr):
        return 0

    best_sum = 0
    current_sum = 0
    for number in arr:
        current_sum  = max(0, current_sum + number)
        best_sum = max(best_sum, current_sum)

    return best_sum


if __name__ == "__main__":
    arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    res = max_sequence(arr)
    print(res)
