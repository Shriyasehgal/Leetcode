class Solution:
    def minimumTotal(self, triangles: List[List[int]]) -> int:
        for i in range(1,len(triangles)):
            for j in range(len(triangles[i])):
                if j == 0:
                    triangles[i][j] += triangles[i-1][j]
                elif j == len(triangles[i])-1:
                    triangles[i][j] += triangles[i-1][j-1]
                else:
                    temp = triangles[i][j]
                    triangles[i][j] = min( triangles[i-1][j-1] + temp, triangles[i-1][j] + temp)
        return min(triangles[-1])