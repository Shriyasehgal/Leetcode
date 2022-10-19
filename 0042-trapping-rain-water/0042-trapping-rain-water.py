class Solution:
    def trap(self, height: List[int]) -> int:
        maxLeft = [0]*len(height)
        maxx = height[0]
        for i in range(len(height)):
            maxx = max(height[i],maxx)
            maxLeft[i] = maxx
            
        maxRight = [0]*len(height)
        maxx = height[-1]
        for j in range(len(height)-1,-1,-1):
            maxx = max(height[j],maxx)
            maxRight[j] = maxx
        res = 0
        for i in range(len(height)):
            if min(maxLeft[i],maxRight[i]) > height[i]:
                res+= min(maxLeft[i],maxRight[i]) - height[i]
        return res
            
            