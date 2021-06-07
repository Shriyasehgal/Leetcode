import re
class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        results= re.findall(r'^\s*[-/+]?\d+',s)
        
        
        if len(results) != 0:
            number= int(results[0])
            if number >= 2147483648:
                number = 2147483647
            elif number <= -2147483649:
                number = -2147483648
            return number
        else:
            return 0
