'''Given an n-ary tree, return the level order traversal of its nodes' values.

Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the null value (See examples).



'''
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]

        """

        if root == None:
            return []


        queue=[]
        qu=[]
        res=[]
        result=[]
        queue.append([root])


        while queue[0]:
            current = queue.pop(0)

            for i in current:
                qu.extend(i.children)
                res.extend([i.val])


            queue.append(qu)
            result.append(res)

            qu =[]
            res = []


        return result
