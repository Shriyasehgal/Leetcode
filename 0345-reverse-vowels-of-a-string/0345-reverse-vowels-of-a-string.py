class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        i, j = 0, len(s)-1
        vowels = set(['a','e','i','o','u','A','E','I','O','U'])
        while i<j:
            while i < len(s) and s[i] not in vowels:
                i+=1
            while j > 0 and s[j] not in vowels:
                j-=1
            if i>=j: break
            s[i], s[j] = s[j], s[i]
            i+=1
            j-=1
        return ''.join(s)
        