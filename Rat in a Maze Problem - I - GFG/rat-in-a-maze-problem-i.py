#User function Template for python3

class Solution:
    def findPath(self, m, n):
        # code here
        if m[0][0] == 0: return []
        totalPaths = []
        r = len(m)
        c = len(m[0])
        def dfs(i,j,visited, path):
            if i == r-1 and j == c-1: 
                totalPaths.append(path)
                return
            if (i,j) in visited: return
            visited.add((i,j))
            if i > 0 and m[i-1][j] == 1:
                dfs(i-1,j,visited,path+'U')
            if i < r-1 and m[i+1][j] == 1:
                dfs(i+1,j,visited,path + 'D')
            if j > 0 and m[i][j-1] == 1:
                dfs(i,j-1,visited,path+'L')
            if j < c-1 and m[i][j+1] == 1:
                dfs(i,j+1,visited,path+'R')
            visited.remove((i,j))
        dfs(0,0,set(),'')
        return totalPaths
            
            

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        
        matrix = [[0 for i in range(n[0])]for j in range(n[0])]
        k=0
        for i in range(n[0]):
            for j in range(n[0]):
                matrix[i][j] = arr[k]
                k+=1
        ob = Solution()
        result = ob.findPath(matrix, n[0])
        result.sort()
        if len(result) == 0 :
            print(-1)
        else:
            for x in result:
                print(x,end = " ")
            print()
# } Driver Code Ends