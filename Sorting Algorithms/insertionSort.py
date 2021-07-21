'''In Insertion Sort The array is virtually split into a sorted and an unsorted part.
Values from the unsorted part are picked and placed at the correct
 position in the sorted part.'''



def insertionSort(nums):
    for i in range(1,len(nums)):
        j=i-1
        while j>=0 and nums[i]<nums[j]:
            j-=1
        popped_el=nums.pop(i)
        nums.insert(j+1,popped_el)

    print(nums)


insertionSort([7,5,6,4,3,32,3,1,3,4,5,9,8])
