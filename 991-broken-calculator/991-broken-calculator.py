class Solution:
    def brokenCalc(self, startValue: int, target: int) -> int:
        op = 0
        while startValue < target:
            if target%2 == 0:
                target //= 2
            else:
                target +=1
            op+=1
        return op + startValue - target