#To find the second largest element in an array
def second_largest(arr):
    largest = float('-inf')
    second = float('-inf')

    for num in arr:
        if num > largest:
            second = largest
            largest = num
        elif num > second and num != largest:
            second = num

    return second if second != float('-inf') else None

arr = [10, 5, 20, 8, 20]
print(second_largest(arr))



#To check if an array is sorted (in ascending order)
def is_sorted(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True

# Example
arr = [1, 2, 3, 4, 5]
print(is_sorted(arr))  