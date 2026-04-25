class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a,b = int(a,2) , int(b,2)

        while b:
            wout_c = a^b
            carray = (a&b) << 1
            a,b = wout_c,carray


        return bin(a)[2:]