class Solution:
    def knightDialer(self, n: int) -> int:
        mod = 1000000007
        res = [1]*10
        temp = []
        paths = {1:[8,6],2:[7,9],3:[4,8],4:[3,9,0],5:[],6:[1,7,0],7:[2,6],8:[1,3],9:[4,2],0:[4,6]}
        k = 1
        while k < n: 
            temp = res[:]
            res = [0]*10
            for i in range(10):
                for j in paths[i]:
                    res[i] += temp[j]
            k+=1
        return sum(res)%mod
                
            
       
            