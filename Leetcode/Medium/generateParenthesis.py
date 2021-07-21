'''Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

 

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]
'''


class Solution(object):
    def __init__(self):
        self.dictP={')':'('}
        self.res=[]
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        par='('
        self.helper(n,par)
        return self.res
    
    def helper(self,n,par,nex=''):
        par=par+nex
        stack_check=[]
        if par.count('(')==par.count(')')==n:
            i=0
            while i<len(par):
                if par[i]=='(':
                    stack_check.append('(')
                elif stack_check[-1]==self.dictP[par[i]]:
                    stack_check.pop()
                i+=1
            if stack_check ==  []:
                self.res.append(par)
                return
            else: return 
            
        if len(par)<2*n:
            if par.count('(')<n:
                self.helper(n,par,'(')
            if par.count(')')<n and par.count(')')<par.count('('):
                self.helper(n,par,')')
