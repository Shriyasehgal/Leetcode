class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = 'aeiouAEIOU'
        left, right = 0, 0
        for i in range(len(s)//2):
            if s[i] in vowels:
                left += 1
        for i in range(len(s)//2,len(s)):
            if s[i] in vowels:
                right +=1
        return left == right
        