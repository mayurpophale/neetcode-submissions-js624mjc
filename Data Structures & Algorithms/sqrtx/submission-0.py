class Solution:
    def mySqrt(self, x: int) -> int:
        L,R = 1,x
        while L<=R:
            M = (L+R) // 2
            M_SQ = M*M

            if M_SQ == x:
                return M
            elif M_SQ < x:
                L = M+1
            else:
                R = M-1
        return R