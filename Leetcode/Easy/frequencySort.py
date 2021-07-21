'''Given a string s, sort it in decreasing order based on the frequency of characters, and return the sorted string.'''

class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        res=''
        c=Counter(s)
        for i in c.most_common():
            res=res+i[0]*i[1]
        return res
