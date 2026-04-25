class Solution:
    def largestGoodInteger(self, num: str) -> str:
        ans = ""
        for i in range(len(num)-2):
            if num[i] == num[i+2] == num[i+1]:
                if ans == "" or num[i] > ans[0]:
                    ans = num[i]*3
        
        return ans