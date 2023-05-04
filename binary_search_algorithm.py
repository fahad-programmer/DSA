def binary_search_algorithm(arr, target):
    """
    *Args (arr, target)

     -> arr -> The array that is sorted in which we have to search
     -> target -> The target which we have to find

    *Return
     -> The index of the target 

    *Important*
     ->  Must have a time complexity of O(Log N)

    """

    left = 0
    right = len(arr) - 1

    while left <= right:

        
        
        middle = (left + right) // 2

        print(f"The middle is {middle}, The Left Is {left}, And The Right Is {right} And Arr Item Is {arr[middle]}")

        if arr[middle] == target:
            return middle
        elif arr[middle] < target:
            left = middle + 1
        else:
            right = middle - 1

        

    return -1


binary_search_algorithm([1, 3, 5, 7, 9, 12, 44], 9)