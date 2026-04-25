class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dict = {
            "(":")",
            "[":"]",
            "{":"}"
        }
        for i in s:
            if i in dict: #Only key values (,{,[ 
                stack.append(dict[i])
            else:
                if not stack or stack.pop() != i:
                    return False
        return not stack