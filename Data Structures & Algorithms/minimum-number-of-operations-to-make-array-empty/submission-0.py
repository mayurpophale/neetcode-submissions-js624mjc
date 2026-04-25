from collections import Counter
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        freq = Counter(nums)
        operations = 0

        for f in freq.values():
            if f == 1:
                return -1
            operations += (f + 2) // 3

        return operations