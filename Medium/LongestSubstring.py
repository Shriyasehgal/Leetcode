class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0
        res=1
        i=1
        j=0
        while i<len(l):
            if l[i] not in temp:
               # temp.append(l[i])
                i+=1
            else:
               # r.append(temp)
                #temp=[]
                temp = l.index(l[i],j,i-1)+1
                j=i
                #temp.append(l[i])
                i=i+1
                res=max(res,temp)
                
            if i== len(l):
                r.append(temp)
        return max(len(x) for x in r)
        
