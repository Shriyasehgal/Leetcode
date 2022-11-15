from collections import deque 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        if k == 0:
            return [target.val]
        treeGraph = defaultdict(list)
        def helper(root):
            if root == None: return
            if root.left:
                treeGraph[root.val].append(root.left.val)
                treeGraph[root.left.val].append(root.val)
                helper(root.left)
            if root.right:
                treeGraph[root.val].append(root.right.val)
                treeGraph[root.right.val].append(root.val)
                helper(root.right)
        helper(root)
        
        q1 = deque([target.val])
        q2 = deque([])
        level = 0
        visited = set([target.val])
        while q1:
            node = q1.popleft()
            for n in treeGraph[node]:
                if n not in visited:
                    q2.append(n)
                    visited.add(n)
            if not q1:
                level+=1
                if level == k:
                    return list(q2)
                q1,q2 = q2,q1
        return []
        