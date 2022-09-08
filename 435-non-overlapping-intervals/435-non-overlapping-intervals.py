from heapq import heapify
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        endVal = intervals[0][1]
        res = 0
        for start,end in intervals[1:]:
            if endVal > start:
                endVal = min(endVal,end)
                res+=1
            else:
                endVal = end
        return res
            
            
        
            