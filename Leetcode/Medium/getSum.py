'''Given two integers a and b, return the sum of the two integers without using the operators + and -.'''


class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        sign=1
        if (a == 0): return b
        if (b == 0): return a
        
        if (a<0 and abs(a)>abs(b)) or (b<0 and abs(a)<abs(b)):
            sign = -1
            
            
            
        if (a<0) != (b<0):
            if abs(a)<abs(b):
                a=a^b
                b=a^b
                a=a^b
            a=abs(a)
            b=abs(b)
            
            while b != 0:
                bor = (~a) & b
                a = a ^ b
                b = bor << 1
            
        else:
            a=abs(a)
            b=abs(b)
            while(b!=0):
                car=a&b
                a=a^b
                b=(car)<<1
        return sign*a
