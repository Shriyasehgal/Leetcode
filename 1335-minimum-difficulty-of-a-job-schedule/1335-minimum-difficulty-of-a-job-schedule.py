class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        if d > len(jobDifficulty): return -1
        memo = {}
        def dfs(i,k):
            if (i,k) in memo: return memo[(i,k)]
            if k == d:
                return max(jobDifficulty[i:]) 
            res = float('inf')
            for j in range(i,len(jobDifficulty)-d+k):
                maxVal = max(jobDifficulty[i:j+1])
                res = min(res, maxVal + dfs(j+1,k+1))
            memo[(i,k)] = res
            return res
        
        return dfs(0,1)
        
                