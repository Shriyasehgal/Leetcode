class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        final_res = []
        def helper(i,res):
            final_res.append(res)
            if i >= len(nums):
                return
            for j in range(i, len(nums)):
                helper(j+1,res+[nums[j]])
        helper(0,[])
        return final_res