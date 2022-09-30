class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        hours = 0
        res = r
        while l <= r:
            k = int((l+r)/2)
            hours = 0
            for i in range(len(piles)):
                hours += ceil(piles[i]/(k))
            if hours <= h:
                res = min(res,k)
                r = k-1
            else:
                l = k+1
        return res