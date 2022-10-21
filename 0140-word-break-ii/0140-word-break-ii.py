class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        dp = [[] for i in range(len(s)+1)]
        dp[0] = [[]]
        for i in range(len(dp)):
            if dp[i]!=[]:
                for word in wordDict:
                     if word == s[i:i+len(word)]:
                        for comb in dp[i]:
                            comb = comb + [word]
                            dp[i+len(word)].append(comb)
        return [' '.join(i) for i in dp[-1]]