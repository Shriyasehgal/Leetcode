class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        i = 0
        j = 0
        s_dict = Counter(s)
        letter = set()
        res = []
        while j < len(s):
            s_dict[s[j]] -= 1
            letter.add(s[j])
            if s_dict[s[j]] == 0:
                letter.remove(s[j])
                if not letter: 
                    res.append(j-i+1)
                    i = j + 1
            j += 1
        return res
                
            
        