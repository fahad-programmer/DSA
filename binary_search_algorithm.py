def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    
    while left <= right:
        middle = (left + right) // 2
        print("middle:", middle)
        
        if arr[middle] == target:
            print("target found at index", middle)
            return middle
        elif arr[middle] < target:
            print("target is in right half of array")
            left = middle + 1
        else:
            print("target is in left half of array")
            right = middle - 1
    
    print("target not found in array")
    return -1
