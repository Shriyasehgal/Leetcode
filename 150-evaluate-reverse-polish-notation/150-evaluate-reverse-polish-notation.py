class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        op = {'+': lambda x,y:x+y,
              '-': lambda x,y:x-y,
              '*': lambda x,y:x*y,
              '/': lambda x,y:int(x/y)}
        for i in range(len(tokens)):
            if tokens[i] not in op:
                stack.append(int(tokens[i]))
            else:
                val1 = stack.pop()
                val2 = stack.pop()
                val3 = op[tokens[i]](val2,val1)
                stack.append(val3)
        return stack.pop()
        