class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        l = {i for i in range(1,len(nums)+1)}
        l1 = set(nums)

        l2 = list(l-l1)

        return l2
