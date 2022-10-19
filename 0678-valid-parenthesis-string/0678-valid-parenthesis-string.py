class Solution:
    def checkValidString(self, s: str) -> bool:
        paraStack = []
        starStack = []
        i = 0
        for c in s:
            if c == '(':
                paraStack.append(i)
            elif c == '*':
                starStack.append(i)
            else:
                if paraStack:
                    paraStack.pop()
                elif starStack:
                    starStack.pop()
                else:
                    return False
            i+=1
        while paraStack and starStack:
            if paraStack and paraStack[-1] < starStack[-1]:
                    paraStack.pop()
            starStack.pop()
        return not paraStack
            