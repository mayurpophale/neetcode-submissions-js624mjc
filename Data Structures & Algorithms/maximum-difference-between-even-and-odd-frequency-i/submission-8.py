from collections import Counter
class Solution:
    def maxDifference(self, s: str) -> int:
        frq = Counter(s)
        mx_odd = float('-inf')
        mi_even = float('inf')
        for i in frq.values():
            if i%2==0:
                mi_even = min(mi_even,i)
            else:
                mx_odd = max(mx_odd,i)

        return mx_odd-mi_even
