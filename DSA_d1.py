#Python program to find the largest element in an array (list)
arr = [10, 25, 5, 78, 30]

largest = max(arr)

print("Largest element:", largest)





# Python Code (Brute Force)

arr = [10, 25, 5, 78, 30]

n = len(arr)

for i in range(n):
    is_largest = True
    
    for j in range(n):
        if arr[j] > arr[i]:   
            is_largest = False
            break
    
    if is_largest:
        print("Largest element:", arr[i])
        break