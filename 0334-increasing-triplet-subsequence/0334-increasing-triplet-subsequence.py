class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        f = float('inf')
        s = float('inf')
        for t in nums:
            if t <= f:
                f = t
            elif t <= s:
                s = t
            else:
                return True
        return False