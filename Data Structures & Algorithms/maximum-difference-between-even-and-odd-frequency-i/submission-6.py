from collections import Counter

class Solution:
    def maxDifference(self, s: str) -> int:
        freq = Counter(s)

        max_even = 0
        max_odd = 0

        for count in freq.values():
            if count % 2 == 0:
                max_even = max(max_even, count)
            else:
                max_odd = max(max_odd, count)

        if max_even == 0 or max_odd == 0:
            return -1

        return max_even - max_odd
