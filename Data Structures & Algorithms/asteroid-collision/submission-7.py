class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for i in asteroids:
            while stack and i<0 and stack[-1]>0: #condition for collision
                diff = i + stack[-1]
                if diff < 0: #magnitude of negative value is greater
                    stack.pop()
                elif diff > 0: #magnitude of negative value is less
                    i=0
                else: #same value
                    i=0
                    stack.pop()
            if i:
                stack.append(i)
        return stack