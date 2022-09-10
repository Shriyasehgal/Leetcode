class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp = [False]*len(nums)
        dp[-1] = True
        goalPost = len(nums)-1
        for i in range(len(nums)-2,-1,-1):
            if i+nums[i]>=goalPost:
                dp[i] = True
                goalPost = i
        return dp[0]