class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        alphabet = 'qwertyuiopasdfghjklzxcvbnm'
        right = Counter(s)
        left = set()
        res = set()
        for char in s:
            right[char] -=1
            for a in alphabet:
                if a in left and right[a] > 0 and a+char+a not in res: res.add(a+char+a)
            left.add(char)
        return len(res)
            
            