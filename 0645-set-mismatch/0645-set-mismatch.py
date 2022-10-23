class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        s = set([i+1 for i in range(len(nums))])
        res = [-1,-1]
        for i in range(len(nums)):
            if nums[i] not in s:
                res[0] = nums[i]
            else:
                s.remove(nums[i])
        res[1] = list(s)[0]
        return res
            
            