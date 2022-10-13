class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = [(s[0],1)]
        count = 0
        for i in range(1,len(s)):
            if stack and s[i] == stack[-1][0]:
                count = stack[-1][1] + 1
                stack.append((s[i],count))
                if count == k:
                    while count: 
                        stack.pop()
                        count-=1
            else:
                stack.append((s[i],1))
        return ''.join([x[0] for x in stack])