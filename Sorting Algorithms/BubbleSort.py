
def bubbleSort(nums):

    for j in range(len(nums)-1,1,-1):
        for i in range(1,j+1):
            if nums[i-1]>nums[i]:
                nums[i-1],nums[i]=nums[i],nums[i-1]           #Swap the adjacent elements if they are in wrong order.

    print (nums)

bubbleSort([5,4,3,5,2,1,4,9,4,3,7,55,4,3,2,4,6,7,9,0,9,3,4,5,4,77,6,5,433,4,72,6,8,8,3,4,5,4,77,6,5,433,4,72,6,8,87,6,6])
