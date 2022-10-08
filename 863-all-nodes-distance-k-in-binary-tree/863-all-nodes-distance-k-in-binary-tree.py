# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
        
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        graph = defaultdict(list)
        res = []
        visited = set()
        def buildGraph(root):
            if root == None: return
            left = root.left if root.left else None
            right = root.right if root.right else None
            if left:
                graph[root.val].append(left.val)
                graph[left.val].append(root.val)
                buildGraph(root.left)
            if right:
                graph[root.val].append(right.val)
                graph[right.val].append(root.val)
                buildGraph(root.right)
        def bst(val, level):
            if level > k : return
            if val in visited: return
            visited.add(val)
            if level == k:
                res.append(val)
            for neigh in graph[val]:
                bst(neigh,level+1)
            
        buildGraph(root)
        bst(target.val,0)
        return res
        
        
                
                
            