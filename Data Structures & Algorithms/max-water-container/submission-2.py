class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        l = 0
        r = n-1
        Max_area = 0

        while l<r:
            h = min(heights[l],heights[r])
            w = r-l
            a = w*h
            Max_area = max(Max_area,a)

            if heights[l] <= heights[r]:
                l +=1
            else:
                r -=1
        
        return Max_area