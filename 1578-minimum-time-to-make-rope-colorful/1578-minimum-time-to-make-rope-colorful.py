class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        s = colors[0]
        minn = [neededTime[0]]
        for i in range(1,len(colors)):
            if colors[i] == s[-1]:
                minn[-1] = max(minn[-1],neededTime[i])
            else:
                minn.append(neededTime[i])
                s+=colors[i]
        return sum(neededTime) - sum(minn)
        
        