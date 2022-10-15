class Solution:
    def maxDepth(self, s: str) -> int:
        curr = 0
        maxx = 0
        for i in s:
            if i == '(':
                curr += 1
            elif i == ')':
                curr -= 1
            maxx = max(maxx,curr)
        return maxx
            