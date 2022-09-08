from collections import Counter
class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        c = Counter(arr)
        for key,val in c.items():
            if val == 1:
                k-=1
                if k == 0:
                    return key
        return ''