class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        i = 1
        while i < len(words):
            dictt = defaultdict(lambda:0)
            if len(words[i]) == len(words[i-1]):
                for j in range(len(words[i])):
                    dictt[words[i][j]] +=1
                    dictt[words[i-1][j]] -=1
                if all(i==0 for i in dictt.values()): 
                    words.pop(i)
                    continue
            i+=1
        return words
        
                