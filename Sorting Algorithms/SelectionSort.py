'''The selection sort algorithm sorts an array by repeatedly finding the minimum element
 (considering ascending order) from unsorted part and putting it at the beginning.'''

def SelectionSort(nums):
    for i in range(0,len(nums)):
        minn_idx=i                                                      # first element declared minn
        for j in range(i+1,len(nums)):
            if nums[j]<nums[minn_idx]:
                minn_idx=j                                              #Find the minimum element in remaining
        popped_el=nums.pop(minn_idx)
        nums.insert(i,popped_el)
    print(nums)


SelectionSort([7,5,6,4,3,32,3,1,3,4,5,9,8])
