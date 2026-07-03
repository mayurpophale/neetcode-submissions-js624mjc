class Solution:
    def myPow(self, x: float, n: int) -> float:
        expo = n

        if expo<0:
            x = 1/x
            expo = -expo

        ans = 1
        while expo>0:
            if expo%2!=0:
                ans *= x
            x *= x
            expo //= 2

        return ans
