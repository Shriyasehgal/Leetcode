class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        memo = {}
        def helper(i, evenBias):
            if i == len(nums):
                return 0
            if (i,evenBias) in memo: return memo[(i,evenBias)]
            if evenBias:
                memo[(i,evenBias)] = max( helper(i+1,not evenBias) + nums[i], helper(i+1,evenBias))
            else:
                memo[(i,evenBias)] = max( helper(i+1,not evenBias) - nums[i], helper(i+1, evenBias))
            
            return memo[(i,evenBias)]
        return helper(0,True)
        