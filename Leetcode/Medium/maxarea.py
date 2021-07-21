class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        
        i=0
        j=len(height)-1
        max_area=0
        
        while i<j:
            
            if height[i]<height[j]:
                max_area=max(max_area,height[i]*(j-i))
                i+=1
            
            else:
                max_area=max(max_area,height[j]*(j-i))
                j-=1
                
        return max_area

sol=Solution()
sol.maxArea([1,1,3,1,4,9,1])  

