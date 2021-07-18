'''Given an integer array nums, return the number of triplets chosen from the array that can make triangles if we take them as side lengths of a triangle.



Example 1:

Input: nums = [2,2,3,4]
Output: 3
Explanation: Valid combinations are:
2,3,4 (using the first 2)
2,3,4 (using the second 2)
2,2,3
Example 2:

Input: nums = [4,2,3,4]
Output: 4'''
import bisect
class Solution(object):
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)<3:
            return 0
        nums.sort()
        count=0

        for i in range(len(nums)):
            if nums[i]==0: continue
            for j in range(i+1,len(nums)):
                c=nums[i]+nums[j]
                count+=self.binarySearch(nums,j+1,c)
        return count

    def binarySearch(self,nums,s,k):
        pos= bisect.bisect_left(nums, k)
        return pos-s
