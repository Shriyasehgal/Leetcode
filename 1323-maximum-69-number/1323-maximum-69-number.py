class Solution:
    def maximum69Number (self, num: int) -> int:
        num = list(str(num))
        change = 1
        for i in range(len(num)):
            if num[i] == '6' and change == 1:
                num[i] = '9'
                change = 0
        return int(''.join(num))
                
            