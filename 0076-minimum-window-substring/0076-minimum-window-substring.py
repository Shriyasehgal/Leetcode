class Solution:
    def minWindow(self, s: str, t: str) -> str:
        countT = Counter(t)
        window = {k:0 for k,v in countT.items()}
        need = len(countT)
        have = 0
        
        i = 0
        j = 0
        res = [-1,-1]
        lenRes = float('inf')
        while True:
            if need > have:
                if j >= len(s): break
                if s[j] in countT:
                    window[s[j]] += 1
                    if window[s[j]] == countT[s[j]]:
                        have+=1
                j+=1
            else:
                if j-i < lenRes:
                    res = [i,j]
                    lenRes = j-i
                if s[i] in window:
                    window[s[i]] -=1
                    if window[s[i]] < countT[s[i]]:
                        have -= 1
                i+=1
                
        return s[res[0]:res[1]]
                