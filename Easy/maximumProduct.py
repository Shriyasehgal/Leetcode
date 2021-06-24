'''Given an integer array nums, find three numbers whose product is maximum and return the maximum product.'''
class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        i=0
        j=len(nums)-1
        pro1=nums[i]*nums[i+1]*nums[j]
        pro2=nums[j]*nums[j-1]*nums[j-2]
        
        if pro1>pro2:
            return pro1
        else:
            return pro2
