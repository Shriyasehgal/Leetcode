class UndergroundSystem(object):

    def __init__(self):
        self.customerId = defaultdict(lambda : [])
        self.stations = defaultdict(lambda : [])

    def checkIn(self, id, stationName, t):
        """
        :type id: int
        :type stationName: str
        :type t: int
        :rtype: None
        """
        self.customerId[id].append((stationName, t))
        

    def checkOut(self, id, stationName, t):
        """
        :type id: int
        :type stationName: str
        :type t: int
        :rtype: None
        """
        
        sourceStation = self.customerId[id][-1][0]
        sourceTime = self.customerId[id][-1][1]
        self.stations[(sourceStation,stationName)].append(t-sourceTime)
        

    def getAverageTime(self, startStation, endStation):
        """
        :type startStation: str
        :type endStation: str
        :rtype: float
        """
        times = self.stations[(startStation, endStation)]
        return float(sum(times))/len(times)
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)