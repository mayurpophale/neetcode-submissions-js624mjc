class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        mx_count = 0
        for i in nums:
            if i == 1:
                count += 1
                mx_count = count if count>mx_count else mx_count
            else:
                count = 0
        return mx_count
        
