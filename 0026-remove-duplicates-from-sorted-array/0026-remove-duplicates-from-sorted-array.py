class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0 
        j = 0 
        
        while j < len(nums):
            curr = nums[j]
            while j < len(nums) and nums[j] == curr:
                j+=1
            nums[i] = curr
            i+=1
        return i