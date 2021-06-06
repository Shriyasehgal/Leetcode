class Solution(object):
     def maxArea(self, height):
        if not height:
            return 0

        left, right = 0, len(height) - 1
        area = 0
        while left < right:
            width = right - left
            if height[left] <= height[right]:
                area = max(area, width * height[left])
                left += 1
            else:
                area = max(area, width * height[right])
                right -= 1
        return area

sol=Solution()
sol.maxArea([1,1,3,1,4,9,1])  

