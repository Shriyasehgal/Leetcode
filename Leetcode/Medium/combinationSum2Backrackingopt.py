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
        summ=sum(candidates)
        if summ==target:return [candidates]
        if summ<target:return []
        candidates.sort()
        self.helper(candidates,target,[],0)
        print(self.all_res)
        return self.all_res

    def helper(self,nums,k,res,curr_sum):

        if curr_sum==k:                                       #feasible solution found
            self.all_res.append(res[:])

        for i in range(len(nums)):
            if i!=0 and nums[i]==nums[i-1]: continue           # multiple copies of the same result
            if curr_sum+nums[i]<=k:
                res.append(nums[i])
                self.helper(nums[i+1:],k,res,curr_sum+nums[i])
                res.pop()
