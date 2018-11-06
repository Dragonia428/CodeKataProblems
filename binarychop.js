function binarySearch(arr, n, target)
{
    start = 0;
    end = n - 1;
    while(start <= end)
    {
        var mid = (start + end) / 2;
        if(arr[mid] == target)
            return mid;
        else if(arr[mid] < target)
            start = mid + 1;
        else 
            end = mid - 1;
    }
    return -1;
}
function binarySearchrecursive(arr, start, end, target)
{
    if(start != 0 || end != arr.length - 1) throw("Start/end is not formatted correctly");
    if(start <= end)
    {
        var mid = (start + end) / 2;
        if(arr[mid] == target)
            return mid;
        else if(arr[mid] < target)
            return binarySearchrecursive(arr, mid +1, end, target);
        else 
            return binarySearchrecursive(arr, start, mid-1, target);
    }
    return -1;
    
}
var arr = [1, 2, 3, 4, 5];
console.log(binarySearchrecursive(arr, 0, arr.length - 1, 3));