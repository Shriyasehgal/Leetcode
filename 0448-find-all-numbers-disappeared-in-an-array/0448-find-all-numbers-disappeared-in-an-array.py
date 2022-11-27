class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        i = 0
        while i < len(nums):
            idx = nums[i]-1
            if nums[i] == nums[idx]:
                i+=1
            else:
                nums[i], nums[idx] = nums[idx], nums[i]
        res = []
        for i in range(len(nums)):
            if nums[i] != i+1:
                res.append(i+1)
        return res