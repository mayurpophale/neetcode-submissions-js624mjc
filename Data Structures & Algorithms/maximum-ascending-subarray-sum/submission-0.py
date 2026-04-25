class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        current = nums[0]
        result = 0
        
        for i in range(1,len(nums)):
            if nums[i-1] < nums[i]:
                current += nums[i]
            else:
                current = nums[i]
            
            result = max(result,current)
        
        return result