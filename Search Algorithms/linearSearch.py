def LinearSearch(arr,key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return -1

LinearSearch([2,3,4,5,6,7,8,9],6)
