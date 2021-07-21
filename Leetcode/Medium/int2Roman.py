'''Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two one's added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given an integer, convert it to a roman numeral.'''

class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        res=''
        j=10
        dict_roman={1:'I',5:'V', 10:'X', 50:'L',100:'C',500:'D',1000:'M'}
        dict_list=list(dict_roman.keys())
        dict_list.sort()
        while num!=0:
            t = num%j
            num=num-t
            if t==0:
                j*=10
                continue
                
            if t in dict_roman.keys():
                res=dict_roman[t]+res
                
            elif t+(j/10) in dict_roman.keys():
                res=dict_roman[(j/10)]+ dict_roman[(t+(j/10))] +res
            
            else:
                k=0
                i=0
                while i<len(dict_list) and dict_list[i]<t:
                    k=dict_list[i]
                    i+=1
                if (k*10)/j ==5:
                    t=t-k
                    t=int((t*10)/j)
                    
                    res = dict_roman[5*j/10]+dict_roman[(j/10)]*t+res
                else:
                    t=int((t*10)/j)
                   
                    res=dict_roman[(j/10)]*t+res
            
            j*=10
                
        return res
