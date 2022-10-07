class MyCalendarThree:

    def __init__(self):
        self.calender = []
        

    def book(self, start: int, end: int) -> int:
        insort(self.calender,[start,1])
        insort(self.calender,[end,-1])
        ans = 0
        cur = 0
        for time,status in self.calender:
            cur+=status
            ans = max(cur,ans)
        return ans

# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(start,end)