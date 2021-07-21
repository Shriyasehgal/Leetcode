'''Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.'''

class Solution(object):
    def __init__(self):
        self.all_res=[]
        self.memo={}

    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.helper(candidates,target,[],0,0)
        candidates.sort()
        return self.all_res

    def helper(self,nums,k,res,curr_sum,i):


        if curr_sum==k:
            res_copy=res[:]
            res_copy.sort()
            if res_copy not in self.all_res:
                self.all_res.append(res_copy)
            return
            
        if curr_sum==k:                   #feasible
            self.all_res.append(res[:])
            return

        elif curr_sum>k:
            return

        if i>=len(nums):
            return

        res.append(nums[i])
        curr_sum+=nums[i]
        self.helper(nums,k,res,curr_sum,i+1)
        res.pop()
        curr_sum-=nums[i]
        self.helper(nums,k,res,curr_sum,i+1)
