class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1): return False
        s1count = [0]*26
        for i in range(len(s1)):
            s1count[ord(s1[i])-ord('a')] +=1
        i = 0
        j = 0
        s2count = [0]*26
        while j < len(s2):
            # creating a window of size s1
            while j < len(s2) and j-i < len(s1):
                s2count[ord(s2[j])-ord('a')] +=1
                j+=1
                
                
            #Checking if the windows is a permuation of s1
            if s1count == s2count:
                return True
            #Shifting the window forward with one element
            else:
                s2count[ord(s2[i])-ord('a')] -=1
                i+=1
        return False
            