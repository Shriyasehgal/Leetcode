
'''QuickSort is a Divide and Conquer algorithm. It picks an element as pivot
and partitions the given array around the picked pivot. There are many different versions of quickSort that pick pivot in different ways. '''

def partition(nums,l,h):
    pivot=nums[l]                    # Position of Pivot is the first element
    i=l

    for j in range(l+1,h+1):
        if nums[j]<pivot:             #Partioning Loop
            i+=1
            nums[j],nums[i]=nums[i],nums[j]


    nums[i],nums[l]=nums[l],nums[i]    ##Brings pivot to it's appropriate position
    return i

def quickSort(nums,l,h):
    if l>=h:
        return

    pivot=partition(nums,l,h)         #pivot position is set to appropriate place

    quickSort(nums,l,pivot-1)         #Sorts the elements to the left of pivot
    quickSort(nums,pivot+1,h)         #Sorts the elements to the right of pivot


nums=[7,5,6,4,3,32,3,1,3,4,5,9,8,4,5,6,87,9,7,65,4,3,4,5,7,8,64,3,34,4,3,2,6,778,6,5,7,5,6,4,3,32,3,1,3,4,5,9,8,4,5,6,87,9,7,65,4,3,4,5,7,8,64,3,34,4,3,2,6,778,6,5]
quickSort(nums,0,len(nums)-1)
