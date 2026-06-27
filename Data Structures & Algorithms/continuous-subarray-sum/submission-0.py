class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        dict = {0:-1}
        
        pre_sum = 0
        for i in range(len(nums)):
            pre_sum +=nums[i]
            remainder = pre_sum %k

            if remainder in dict:
                if (i-dict[remainder]) >= 2:
                    return True
                else:
                    dict[remainder] = i
                

        return False
        