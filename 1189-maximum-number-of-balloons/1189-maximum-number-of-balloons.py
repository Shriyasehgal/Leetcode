class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        textDict = Counter(text)
        balloonDict = Counter('balloon')
        minn = float('inf')
        for k,val in balloonDict.items():
            if k not in textDict: return 0
            minn = min(minn,textDict[k]//val)
        return minn        