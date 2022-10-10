class Solution:
    def isPalindrome(self, word):
        return word == word[::-1] or len(word) == 0
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        pairs = []
        words = {word:i for i,word in enumerate(words)}
        for word in words.keys():
            for j in range(len(word)+1):
                pref = word[:j]
                suff = word[j:]
                if self.isPalindrome(pref): 
                    temp = suff[::-1]
                    if temp!=word and temp in words.keys():
                        pairs.append([words[temp],words[word]])
                #This is to leave out the empty string.
                if j!=len(word) and self.isPalindrome(suff):
                    temp = pref[::-1]
                    if temp!=word and temp in words.keys():
                        pairs.append([words[word], words[temp]])
        return pairs