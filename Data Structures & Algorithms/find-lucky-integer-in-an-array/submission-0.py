class Solution:
    def findLucky(self, arr: List[int]) -> int:
        l  = []
        for i in arr:
            if i == arr.count(i):
                l.append(i)
            else:
                l.append(-1)
        return sorted(l)[-1]