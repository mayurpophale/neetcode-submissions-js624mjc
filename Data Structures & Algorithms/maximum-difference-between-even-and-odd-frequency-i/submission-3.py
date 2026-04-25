from collections import Counter
class Solution:
    def maxDifference(self, s: str) -> int:
        freq = Counter(s)
        mi_val = 0
        mx_val = 0

        for count in freq.values():
            if count%2==0:
                mx_val = max(mx_val,count)
            else:
                mi_val = max(mi_val,count)

        if mx_val == 0 or mi_val == 0:
            return -1

        return abs( mi_val- mx_val)