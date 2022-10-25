class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        i1 = j1 = i2 = j2 = 0
        while i1 < len(word1) and i2< len(word2):
            if word1[i1][j1] != word2[i2][j2]: return False
            j1+=1
            j2+=1
            if j1>=len(word1[i1]): 
                j1 = 0
                i1 += 1
            if j2>= len(word2[i2]):
                j2 = 0
                i2 += 1
            
            if i1 == len(word1) and i2 == len(word2): return True
        return False
                