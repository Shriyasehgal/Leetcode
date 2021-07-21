class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        sol={}
        I=[]
        for i in range(len(nums)):
            complement = target - nums[i]
            if (sol.has_key(complement) and sol[complement]!=i):
                I.append(i)
                I.append(sol[complement])
                return I
        
            sol[nums[i]]=i
            
