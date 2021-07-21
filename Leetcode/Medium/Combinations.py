'''Given two integers n and k, return all possible combinations of k numbers out of the range [1, n].

You may return the answer in any order.'''


class Solution(object):
    def __init__(self):
        self.res=[]
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        self.helper(n,k,[],1)
        return self.res


    def helper(self,n,k,subset,i):

        if len(subset)==k:
            self.res.append(subset[:])
            return
        elif i>n or len(subset)>k:
            return
        else:
            subset.append(i)
            self.helper(n,k,subset,i+1)
            subset.pop()
            self.helper(n,k,subset,i+1)
