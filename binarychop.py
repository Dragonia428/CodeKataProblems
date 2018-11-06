def binarySearch(arr, n, target):

    start = 0
    end = n - 1
    while start <= end:
    
        mid = (start + end) / 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            start = mid + 1
        else: 
            end = mid - 1
    
    return -1

def binarySearchrecursive(arr, start, end, target):

    if start != 0 or end != len(arr) - 1:
         raise("Start/end is not formatted correctly")
    if start <= end:
    
        mid = (start + end) / 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            return binarySearchrecursive(arr, mid +1, end, target)
        else: 
            return binarySearchrecursive(arr, start, mid-1, target)
    
    return -1
    

arr = [1, 2, 3, 4, 5]
print(binarySearchrecursive(arr, 0, len(arr) - 1, 3))