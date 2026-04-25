class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        l = sorted(nums)
        return l[-1]*l[-2] - l[1]*l[0]