class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        l = 0
        Max_area = 0
        r = n-1

        while l<r:
            w = r-1
            h = min(heights[l],heights[r])
            a = w*h
            Max_area = max(a,Max_area)

            if heights[l] < heights[r]:
                l +=1
            else:
                r -=1
        
        return Max_area