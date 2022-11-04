class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        # lee(t(c)o)de)
        #        |
        # stack = [("(",3), ("(",5)]   #('(', i)
        # 
        i = 0
        s = list(s)
        stack = []
        while i < len(s):
            if s[i] == '(':
                stack.append(('(',i))
                i+=1
            elif s[i] == ')':
                if stack:
                    stack.pop()
                    i+=1
                else:
                    s[i] = ''
            else:
                i+=1
            
        while stack:
            s[stack.pop()[1]] = ''
            
        return ''.join(s)
        
                
            
            