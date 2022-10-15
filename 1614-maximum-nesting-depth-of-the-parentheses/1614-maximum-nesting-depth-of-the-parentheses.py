class Solution:
    def maxDepth(self, s: str) -> int:
        stack = []
        maxx = 0
        for i in s:
            if i == '(':
                stack.append(i)
            elif i == ')':
                stack.pop()
            maxx = max(maxx,len(stack))
        return maxx
            