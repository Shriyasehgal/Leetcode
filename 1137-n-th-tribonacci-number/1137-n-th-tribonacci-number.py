class Solution:
    def tribonacci(self, n: int, memo = {}) -> int:
        if n == 0: return 0
        if n <= 2: return 1
        dp = [0]*(n+1)
        dp[1] = 1
        dp[2] = 1
        for i in range(3, len(dp)):
            dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
        return dp[-1]
        
        
        '''if n in memo: return memo[n]
        if n == 0:
            return 0
        if n <= 2:
            return 1
        memo[n] = self.tribonacci(n-1,memo) + self.tribonacci(n-2,memo) + self.tribonacci(n-3,memo)
        return memo[n]'''