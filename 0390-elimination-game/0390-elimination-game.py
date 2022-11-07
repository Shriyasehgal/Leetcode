class Solution:
    def lastRemaining(self, n: int) -> int:
        head = 1
        isLeft = True
        remaining = n
        step = 1
        while remaining > 1:
            if isLeft or remaining%2 == 1:
                head = head + step
            remaining //=2
            step *= 2
            isLeft = not isLeft
        return head