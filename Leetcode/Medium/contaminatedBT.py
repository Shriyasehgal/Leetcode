# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#Using Path
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.root = root

    def find(self, target: int) -> bool:
        root = self.root
        path = []
        while target != 0:
            temp = target % 2
            if temp == 1:
                path = [1] + path
            if temp == 0:
                path = [2] + path
            target = (target-path[0])/2
            
        for i in path:
            if i == 1:
                if root.left:
                    root = root.left
                else:
                    return False
            else:
                if root.right:
                    root = root.right
                else:
                    return False
        return True
            
        
        
#Using Dfs           
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.root = root

    def find(self, target: int) -> bool:
        def helper(root,val):
            if root == None:
                return False
            root.val = val 
            if root.val == target:
                return True
            return helper(root.left,2*root.val+1) or helper(root.right,2*root.val+2)
        return helper(self.root,0)
            


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)
