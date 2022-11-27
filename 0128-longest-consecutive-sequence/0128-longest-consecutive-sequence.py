class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        maxLen = 0
        for i in range(len(nums)):
            if nums[i]-1 in numSet: 
                continue
            else:
                j = nums[i]
                currLen = 0
                while j in numSet:
                    currLen += 1
                    j+=1
                maxLen = max(maxLen, currLen)
        return maxLen
                