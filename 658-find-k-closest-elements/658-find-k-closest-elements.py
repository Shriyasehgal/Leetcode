class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        minVal = float('inf')
        i = 0 
        j = 0
        minValIdx = (i,j)
        windowVal = 0
        while j < len(arr): 
            while j-i+1 <= k:
                windowVal += abs(arr[j]-x)
                j+=1
            if windowVal < minVal:
                minVal = windowVal
                minValIdx = (i,j)
            windowVal -= abs(arr[i]-x)
            i+=1
        return arr[minValIdx[0]:minValIdx[1]]
        
            
                