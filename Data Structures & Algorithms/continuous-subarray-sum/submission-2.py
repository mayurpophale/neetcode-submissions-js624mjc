class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        seen = {0:-1}
        
        pre_sum = 0
        for i in range(len(nums)):
            pre_sum +=nums[i]
            remainder = pre_sum %k

            if remainder in seen:
                if (i-seen[remainder]) >= 2:
                    return True
            else:
                    seen[remainder] = i
                

        return False
