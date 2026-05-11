class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xorr = 0

        for num in nums:
            xorr ^= num

        rightmost = xorr & -xorr

        a = 0
        b = 0

        for num in nums:
            if num & rightmost:
                a ^= num
            else:
                b ^= num

        return [a, b]