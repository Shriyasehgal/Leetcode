'''Given two integers dividend and divisor, divide two integers without using multiplication, division, and mod operator.

Return the quotient after dividing dividend by divisor.

The integer division should truncate toward zero, which means losing its fractional part. For example, truncate(8.345) = 8 and truncate(-2.7335) = -2.'''




class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
         """
        if dividend==0 or abs(dividend)<abs(divisor):
            return 0
        
        if (dividend<0) is not (divisor<0):
            sign = -1
        else:
            sign = 1
        
        a=self.to_binary(abs(dividend))
        b=self.to_binary(abs(divisor))
        q = ''
        r = ''
        i=0
        

        while True:
            temp = '0'
            temp=temp+str(r).lstrip('0')
            while i<len(a) and int(temp)<int(b):
                temp=temp+a[i]
                i+=1
                if int(temp)<int(b):
                    q=q+'0'
            
            if int(temp)>=int(b):
                q=q+'1'
                r= bin(int(temp,2) - int(b,2)).replace("0b", "")   

            if i==len(a): 
                q=int(q.lstrip('0'),2)
                if sign == -1:
                     q=q-q-q
                if -2**31 <=  q  <= 2**31 - 1:
                    return q  
                elif q  >2**31-1:
                    return 2**31-1
                else:
                    return -2**31

                
                
    def to_binary(self,n):
	return bin(n).replace("0b", "")
        return bin(n).replace("0b", "")
    
   

