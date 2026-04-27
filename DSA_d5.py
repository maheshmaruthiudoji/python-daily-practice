#Left rotating an array by D places
def leftRotate(arr, d):
    n = len(arr)
    d = d % n   
    return arr[d:] + arr[:d]

#Example
arr = [1, 2, 3, 4, 5]
print(leftRotate(arr, 2))


#move all the zeros to the end of the array
def moveZeroes(nums):
    j = 0 

    for i in range(len(nums)):
        if nums[i] != 0:
            nums[i], nums[j] = nums[j], nums[i]
            j += 1

    return nums

# Example
arr = [0, 1, 0, 3, 12]
print(moveZeroes(arr))