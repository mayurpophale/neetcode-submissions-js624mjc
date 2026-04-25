class Solution:
    def decodeString(self, s: str) -> str:
        cur_num = 0
        cur_str = ''
        stack = []

        for i in s:
            if i.isdigit():
                cur_num = cur_num*10 + int(i)
            
            elif i == "[":
                stack.append((cur_str,cur_num))
                cur_num = 0
                cur_str = ''
            elif i == "]":
                prev_str,prev_num = stack.pop()
                cur_str = prev_str + prev_num*cur_str
            
            else:
                cur_str +=i
        
        return cur_str