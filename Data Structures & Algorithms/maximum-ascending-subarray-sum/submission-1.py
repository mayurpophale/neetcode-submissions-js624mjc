class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        current = nums[0]
        result = 0
        
        for i in range(1,len(nums)):
            if not (nums[i-1] < nums[i]):
                current = 0
            current += nums[i]
            result = max(result,current)
        
        return result