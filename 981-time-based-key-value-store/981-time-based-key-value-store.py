class TimeMap:

    def __init__(self):
        self.timeMap = defaultdict(list)    
    
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timeMap[key].append((timestamp,value))

    def get(self, key: str, timestamp: int) -> str:
        values = self.timeMap[key]
        l = 0
        r = len(values)-1
        res = (0,'')
        while l<=r:
            m = (l+r)//2
            if values[m][0] == timestamp:
                return values[m][1]
            elif values[m][0] > timestamp:
                r = m-1
            else:
                if res[0] < values[m][0]:
                    res = (values[m][0],values[m][1])
                l = m+1
        return res[1]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)