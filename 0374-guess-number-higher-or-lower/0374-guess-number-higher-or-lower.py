# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        l = 1
        r = n
        while True:
            num = (l+r)//2
            decision = guess(num)
            if decision == 0:
                return num
            elif decision == 1:
                l = num+1
            else:
                r = num-1
        
                
                