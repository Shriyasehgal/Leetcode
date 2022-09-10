class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = [float(inf)]*len(nums)
        dp[-1] = 0
        for i in range(len(nums)-2, -1, -1):
            if nums[i] == 0:
                continue
            dp[i] = min(dp[i+1:i+nums[i]+1]) +1
        return dp[0]