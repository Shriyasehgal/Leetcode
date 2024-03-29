class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        stack.append(s[0])
        for i in range(1,len(s)):
            if stack and abs(ord(s[i])-ord(stack[-1])) == 32:
                stack.pop()
            else:
                stack.append(s[i])
        return ''.join(stack)
            
       