class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        return (self.helper(0,n,k,target,{}))%1000000007
        
    def helper(self,i, n , k , summ, memo):
        if (n,summ) in memo : return memo[(n,summ)]
        if  n < 0 or summ < 0:
            return 0
        if summ == 0 and n==0:
            return 1
        res = 0
        for j in range(1,k+1):
            res+=self.helper(j,n-1,k,summ-j,memo)
        memo[(n, summ)] = res
        return res