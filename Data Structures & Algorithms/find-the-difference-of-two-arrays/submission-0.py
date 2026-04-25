class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        num1set , num2set = set(nums1) , set(nums2)
        res1,res2 = set(),set()

        for i in nums1:
            if i not in num2set:
                res1.add(i)

        for i in nums2:
            if i not in num1set:
                res2.add(i)

        return [list(res1),list(res2)]