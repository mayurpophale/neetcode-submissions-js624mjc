import math
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i in "+-*/":
                b,a = stack.pop(),stack.pop()
                if i == "+":
                    stack.append(a+b)
                elif i == "-":
                    stack.append(a-b)
                elif i == "*":
                    stack.append(a*b)
                else:
                    div = a/b 
                    if div < 0:
                        stack.append(math.ceil(div))
                    else:
                        stack.append(int(div))
            else:
                stack.append(int(i))
        return stack[0]                                        