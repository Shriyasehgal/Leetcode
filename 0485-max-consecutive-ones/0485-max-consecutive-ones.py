class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxOne = 0
        currOne = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                currOne = 0
            else:
                currOne+=1
                maxOne = max(maxOne,currOne)
        return maxOne