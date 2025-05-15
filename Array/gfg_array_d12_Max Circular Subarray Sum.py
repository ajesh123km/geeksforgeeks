def kadane(arr):
    max_sum = float('-inf')
    curr_sum = 0
    for num in arr:
        curr_sum = max(num, curr_sum + num)
        max_sum = max(max_sum, curr_sum)
    return max_sum

def circularSubarraySum(arr):
    max_kadane = kadane(arr)  # Max sum using Kadane's Algorithm

    total_sum = sum(arr)
    for i in range(len(arr)):
        arr[i] = -arr[i]  # Invert the array to find the min sum subarray

    max_wrap = total_sum + kadane(arr)  # Circular max sum

    return max(max_kadane, max_wrap) if max_wrap != 0 else max_kadane

arr = [8, -8, 9, -9, 10, -11, 12]
print(circularSubarraySum(arr))
