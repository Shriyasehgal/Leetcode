class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        if len(cardPoints) == k: return sum(cardPoints)
        i = 0
        j = 0
        n = len(cardPoints)
        summ = sum(cardPoints)
        window = n-k
        maxSum = 0
        currSum = 0
        while j <= n-1:
            while j <= n-1  and (j-i+1) <= window:
                currSum += cardPoints[j]
                j+=1

            maxSum = max(maxSum, summ - currSum)
            currSum -= cardPoints[i]
            i+=1
        return maxSum
            