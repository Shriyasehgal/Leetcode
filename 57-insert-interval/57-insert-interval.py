class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        for i in range(len(intervals)):
            # The new Interval has already been added to the list and 
            # does not overlap with the current interval
            if newInterval[1] < intervals[i][0]:
                
                res.append(newInterval)
                return res + intervals[i:]
            
            #The new Interval has not been added to the list but doesnot 
            # overlap with the current interval
            elif newInterval [0] > intervals[i][1]:
                res.append(intervals[i])
            #The new Interval overlaps with the current interval
            else:
                newInterval = [min(newInterval[0],intervals[i][0]),                                                            max(newInterval[1],intervals[i][1])]
        res.append(newInterval)
        return res