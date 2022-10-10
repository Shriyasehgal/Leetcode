class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome) == 1:
            return ''
            
        res = ''
        broken = False
        
        for i,c in enumerate(palindrome):
            if not broken:
                if i == (len(palindrome)-1)/2 or c == 'a':
                    res += c
                else:
                    res +='a'
                    broken = True
            else:
                res+=c
        if broken: return res
        return res[:-1]+'b'
                
            