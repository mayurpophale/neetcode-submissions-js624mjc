class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        leftS = 0

        for i in range(len(nums)):
            rightS = total - leftS - nums[i]

            if leftS == rightS:
                return i
            
            leftS += nums[i]

        return -1