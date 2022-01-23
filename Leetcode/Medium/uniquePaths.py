class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        final = 0
        memo = {}
        def helper(i,j):
            nonlocal final
            
            if i == m-1 and j == n-1:
                final = 1
                return final
            
                
            if '{} {}'.format(i,j) in memo.keys():
                return memo['{} {}'.format(i,j)]
            
            if i == m-1:
            
                final = helper(i,j+1)
                return final
            
            if j == n-1:
                final = helper(i+1,j)
                return final
            
            final=helper(i+1,j) + helper(i,j+1) 
           
            memo['{} {}'.format(i,j)] = final
            return final
        
        helper(0,0)
        return final
      
     #More optimised way of solving the same question
      class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        dp = [[0 for i in range(n)]for j in range(m)]
        
        for i in range(m):
            dp[i][0]=1
        for j in range(n):
            dp[0][j]=1
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]
        
        
