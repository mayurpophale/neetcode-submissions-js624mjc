class Solution:
    def decodeString(self, s: str) -> str:
        num = 0
        char = ''
        stack = []

        for i in s:
            if i.isdigit():
                num = num*10 + int(i)
            
            elif i == "[":
                stack.append((char,num))
                char = ''
                num = 0
            elif i == "]":
                prev_str,prev_num = stack.pop()
                char = prev_str + prev_num*char
            
            else:
                char +=i
        
        return char