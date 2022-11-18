class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1: return 0
        l = 0
        r = len(nums) - 1
        while l <= r:
            m =  l + (r-l)//2
            if (m-1 < 0 or nums[m-1] < nums[m]) and (m+1 > len(nums)-1 or nums[m+1] < nums[m]):
                return m
            elif m>0 and nums[m-1] > nums[m]:
                r = m - 1
            elif m<len(nums)-1 and nums[m+1] > nums[m]:
                l = m + 1
        