class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        b = sorted(asteroids)
        for i in b[::-1]:
            if i>0:
                stack.append(i)
            elif abs(i) == stack[-1]:
                stack.pop()
            elif abs(i) > stack[-1]:
                stack.pop()
            elif abs(i) < stack[-1]:
                continue
        return stack