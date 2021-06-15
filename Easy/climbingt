'''You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

 

Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step'''

class Solution(object):
    def __init__(self):
        self.d=dict()
        
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==0: return 0
        if n==1: return 1
        if n==2: return 2
        
        if n-1 in self.d.keys():
            count1= self.d[n-1]
        else: count1=self.climbStairs(n-1)
        
        if n-2 in self.d.keys():
            count2= self.d[n-2]
        else: count2 = self.climbStairs(n-2)
            
        self.d[n]=count2+count1
        
        return count1+count2
