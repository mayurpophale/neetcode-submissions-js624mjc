class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        current = str(n)

        while current not in seen:
            seen.add(current)
            summ = 0
            for i in current:
                digits = int(i)
                summ += digits** 2
            
            if summ == 1: return True
            current = str(summ)
        
        return False