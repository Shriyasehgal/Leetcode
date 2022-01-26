class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []
        n = len(candidates)
        listsum = 0
        def helper(i):
            nonlocal listsum
            if i >= n: 
                return []
            if listsum > target:
                return 
            if listsum == target:
                res.append(subset[:])
                return
            
            subset.append(candidates[i])
            listsum += candidates[i]
            helper(i)
            subset.pop()
            listsum -= candidates[i]
            helper(i+1)
            
        helper(0)
        return res
            
   #Optimized solution.
  class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []
        n = len(candidates)
        listsum = 0
        def helper(i):
            nonlocal listsum
            if listsum > target:
                return 
            if listsum == target:
                res.append(subset[:])
            for j in range(i,n):
                listsum += candidates[j]
                subset.append(candidates[j])
                helper(j)
                subset.pop()
                listsum-=candidates[j]
                
            
        helper(0)
        return res
            
