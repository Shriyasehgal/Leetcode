"""Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets."""


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        i=0
        j=len(nums)-1
        results=[]
        k=0
        if len(nums)<=2:
            return []
        
        if nums[0]==0 and nums.count(nums[0])==len(nums):
            return [[0,0,0]]
            
        while nums[i] <=0:
            while nums[j]>=0:
                k= 0-(nums[i]+nums[j])
                if k in nums[i+1:j] and [nums[i],nums[j], k] not in results :
                    results.append([nums[i],nums[j], k])
                j-=1
                if abs(j)==len(nums):
                    break
            i+=1
            j=len(nums)-1
            if abs(i)==len(nums):
                break
        return results  
