class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        s = 0
        max_i = min(nums)
        for i in range(len(nums)):

            s += nums[i]
            if s>max_i:
                max_i = s
            elif s< 0:
                s = 0

        return max_i