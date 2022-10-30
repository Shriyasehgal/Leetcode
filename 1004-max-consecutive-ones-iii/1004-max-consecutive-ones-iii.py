class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        i = 0
        j = 0
        maxx = 0
        n = 0
        while j < len(nums):
            while j < len(nums) and (n < k or nums[j] == 1):
                maxx = max(maxx, j-i+1)
                if nums[j] == 0: n+=1
                j+=1
            if j >= len(nums)-1: break
            while nums[i]!=0:
                i+=1
            i+=1
            n-=1
        return maxx
            