class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l = []

        for i in range(len(s)-1,-1,-1):
            l.append(s[i])

        return l     