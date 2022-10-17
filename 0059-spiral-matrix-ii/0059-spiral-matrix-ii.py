class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        step = 0
        matrix = [[0 for i in range(n)] for j in range(n)]
        l,r = 0, n-1
        u,d = 0, n-1
        curr = 1
        while curr <= n*n:
            match step%4:
                case 0:
                    for i in range(l,r+1):
                        matrix[u][i] = curr
                        curr+=1
                    u+=1
                case 1:
                    for i in range(u,d+1):
                        matrix[i][r] = curr
                        curr+=1
                    r-=1
                case 2:
                    for i in range(r,l-1,-1):
                        matrix[d][i] = curr
                        curr+=1
                    d-=1
                case 3:
                    for i in range(d,u-1,-1):
                        matrix[i][l] = curr
                        curr+=1
                    l+=1
            step+=1
        return matrix
                    