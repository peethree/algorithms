def binary_search(target, arr):
    
    n = len(arr)
    
    low = 0 
    high = n - 1
    
    while low <= high:
        median = (low + high) // 2
    
        if arr[median] == target:
            return True
        else:
            if arr[median] < target:
                low = median + 1
            else:
                high = median - 1
    
    return False