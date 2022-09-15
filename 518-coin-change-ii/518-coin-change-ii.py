class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [[0 for a in range(amount+1)] for c in range(len(coins))]
        for i in range(len(dp)):
            dp[i][0] = 1
            
        for c in range(len(coins)-1,-1,-1):
            for a in range(1,amount+1):
                #Including the current coin c
                if a - coins[c] >= 0:
                    dp[c][a] += dp[c][a-coins[c]]
                #including the current coin c
                if c+1 < len(coins):
                    dp[c][a] += dp[c+1][a]
        return dp[0][amount]
                    