# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:
    def inorder(self, root):
        if root == None: return []
        order = []
        order += self.inorder(root.left)
        order.append(root.val)
        order += self.inorder(root.right)
        return order
        

    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.order = self.inorder(root) 
        self.ptr = 0

    def next(self) -> int:
        val = self.order[self.ptr]
        self.ptr+=1
        return val
        
    def hasNext(self) -> bool:
        if self.ptr < len(self.order): return True
        return False
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()