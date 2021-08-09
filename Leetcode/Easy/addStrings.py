'''Given two non-negative integers, num1 and num2 represented as string, return the sum of num1 and num2 as a string.

You must solve the problem without using any built-in library for handling large integers (such as BigInteger). You must also not convert the inputs to integers directly.

 '''
class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """

        res=''
        carry = '0'
        i=-1

        num1 = num1.zfill(max(len(num1),len(num2)))
        num2 = num2.zfill(max(len(num1),len(num2)))

        while -i<=len(num1):

            k = str((ord(num1[i]) + ord(num2[i]) + int(carry) - 2*ord('0')))
            carry = '0'

            if len(k)>1:
                carry = k[0]
                k=k[1]

            res=k+res
            i-=1
        if carry == '1':
            res = carry + res

        return res
