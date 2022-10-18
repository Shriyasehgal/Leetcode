class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        #This question will be solved using Union Find
        parent = [i for i in range(n)]
        components = n
        def find(x):
            if x == parent[x]: return parent[x]
            return find(parent[x])
        
        def union(x,y):
            nonlocal components
            x = find(x)
            y = find(y)
            if x == y:
                return False
            else:
                components -=1
                parent[y] = x
                return True
        
        for i in range(n):
            if leftChild[i] != -1:
                if parent[leftChild[i]] != leftChild[i]: return False
                if not union(i,leftChild[i]): return False
            if rightChild[i] != -1:
                if parent[rightChild[i]] != rightChild[i]: return False
                if not union(i,rightChild[i]): return False
        if components!= 1: return False
        return True
            
        