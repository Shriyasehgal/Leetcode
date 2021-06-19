'''Given a binary string s, return true if the longest contiguous segment of 1s is strictly longer than the longest contiguous segment of 0s in s. Return false otherwise.

For example, in s = "110100010" the longest contiguous segment of 1s has length 2, and the longest contiguous segment of 0s has length 3.
Note that if there are no 0s, then the longest contiguous segment of 0s is considered to have length 0. The same applies if there are no 1s.'''
class Solution(object):
    def checkZeroOnes(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s)==1 :
            return bool(int(s))

        i=0
        j=1
        count={'0':0,'1':0}
        while j<len(s):

            if s[i]==s[j]:
                j+=1
                if count[s[i]]<(j-i):
                    count[s[i]]=j-i
            else:
                i=j
                j+=1

        if count['1']>count['0']:
            return True
        return False
