class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit=0
        max_profit=0
        tot_pro=0
        s=0
        e=0
        for i in range(1,len(prices)):
            profit=prices[i]-prices[s]
            if i==s:
                continue
            if profit<0:
                s=i
                e=i
                continue
                        
            if max_profit<profit:
                max_profit=profit
                e=i
            
            if i<len(prices)-1 and prices[i+1]<prices[i]:
                s=i+1
                e=i+1
                tot_pro+=max_profit
                max_profit=0
            
        return tot_pro+max_profit
        
sol=Solution()
sol.maxProfit([7,1,5,3,6,4,2])
