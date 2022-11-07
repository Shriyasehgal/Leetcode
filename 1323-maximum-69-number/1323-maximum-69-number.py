class Solution:
    def maximum69Number (self, num: int) -> int:
        k, i  = 0, 1
        while i < num:
            if num // i % 10 == 6:
                k = i
            i*=10
        return num + 3*k
                
            