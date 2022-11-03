class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        c = Counter(words)
        res = 0
        double = 0
        checked = set()
        for word in c:
            if word in checked: continue
            revWord = word[::-1]
            if word == revWord:
                if c[word]%2 == 0:
                    res+=c[word]
                else:
                    res+=(c[word]-1)
                    double = 1
            elif revWord in c: 
                res += 2*min(c[word],c[revWord])
            checked.add(word)
            checked.add(revWord)
        return 2*(res+double)