class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subset = []
        final = []
        def helper(i):
         
            if i >= len(nums):
                final.append(subset[:])
                return
            subset.append(nums[i])
            helper(i+1)
            subset.pop()
            helper(i+1)
        helper(0)
        return final
