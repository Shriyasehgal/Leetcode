class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum=nums[0]
        max_sum= nums[0]
        s=0
        e=0
        for i in range(1,len(nums)):
            sum+=nums[i]
            if sum<nums[i]:
                sum=nums[i]
                s=i
                
            if max_sum<sum:
                max_sum=sum
                e=i
                
                
        return max_sum
        
sol=Solution()
sol.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
