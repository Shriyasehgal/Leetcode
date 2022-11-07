# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root: return []
        levelDict = defaultdict(list)
        tempDict = defaultdict(list)
        oldQueue = [(root,0)]
        newQueue = []

        res = []
        Minn, Maxx = 0,0
        while oldQueue:
            elem = oldQueue.pop(0)
            if elem[0].left:
                Minn = min(Minn, elem[1]-1)
                newQueue.append((elem[0].left,elem[1]-1)) 
            if elem[0].right:
                Maxx = max(Maxx, elem[1]+1)
                newQueue.append((elem[0].right, elem[1]+1)) 
            tempDict[elem[1]].append(elem[0].val)
            if not oldQueue:
                for d in tempDict: levelDict[d].extend(sorted(tempDict[d]))
                newQueue,oldQueue = oldQueue,newQueue
                tempDict.clear()
        for i in range(Minn, Maxx+1):
            res.append(levelDict[i])
        return res