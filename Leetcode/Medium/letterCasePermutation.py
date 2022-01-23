class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        final = []
    
        s = list(s)
        
        def helper(i):
            if i == len(s):
                final.append(''.join(s[:]))
                return
            if ord(s[i]) < 65:
                helper(i+1)
            else:
                s[i] = s[i].upper()
                helper(i+1) 
                s[i] = s[i].lower()
                helper(i+1)
        helper(0)
        return final
