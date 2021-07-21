class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        carry=1
        i=-1
        
        while carry==1:
            if digits[i]==9:
                digits[i]=0
                i-=1
        
            else:
                digits[i]=digits[i]+1
                return digits
            
            if abs(i+1)==len(digits):
                return [1] + digits
        
