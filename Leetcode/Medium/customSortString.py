'''order and str are strings composed of lowercase letters. In order, no letter occurs more than once.

order was sorted in some custom order previously. We want to permute the characters of str so that they match the order that order was sorted. More specifically, if x occurs before y in order, then x should occur before y in the returned string.

Return any permutation of str (as a string) that satisfies this property.

Example:
Input:
order = "cba"
str = "abcd"
Output: "cbad"
Explanation:
"a", "b", "c" appear in order, so the order of "a", "b", "c" should be "c", "b", and "a".
Since "d" does not appear in order, it can be at any position in the returned string. "dcba", "cdba", "cbda" are also valid outputs.'''


class Solution(object):
    def customSortString(self, order, str):
        """
        :type order: str
        :type str: str
        :rtype: str
        """


        counter_str=Counter(str)
        res=''


        for letter in order:                                 #letters in order
            if letter in counter_str.keys():
                res=res+letter*counter_str[letter]
                counter_str.pop(letter)

        for i in counter_str.keys():                          #Rest of the letters
            res=res+i*counter_str[i]
            #counter_str.pop(i)

        return res
