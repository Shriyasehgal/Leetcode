class Solution:
    def maxRepOpt1(self, text: str) -> int:
        mapp = defaultdict(list)
        for i,c in enumerate(text):
            mapp[c].append(i)
        res = 0
        for m in mapp.values():
            curr = 1
            pre = 0
            maxL = 0
            for i in range(1, len(m)):
                if m[i] == m[i-1] + 1:
                    curr +=1
                else:
                    if m[i] == m[i-1] + 2:
                        pre = curr
                        
                    else:
                        pre = 0
                    curr = 1
                maxL = max(maxL,pre+curr)                  
            if maxL < len(m): maxL +=1
            res = max(maxL, res)
        return res
            