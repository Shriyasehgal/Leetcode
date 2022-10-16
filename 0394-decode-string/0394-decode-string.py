class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        res = ''
        num = 0
        for i in range(len(s)):
            if s[i] == '[':
                stack.append(res)
                stack.append(num)
                res = ''
                num = 0
            elif s[i] == ']':
                currNum = stack.pop()
                prevRes = stack.pop()
                res = prevRes + currNum*res
            elif s[i].isdigit():
                num = num*10 + int(s[i])
            else:
                res+=s[i]
        return res
                    
                
        
                    
            