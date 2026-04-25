class Solution:
    def carFleet(target, position, speed):
        cars = list(zip(position, speed))
        cars.sort(reverse=True)  # sort by position descending
    
        stack = []
    
        for pos, spd in cars:
            time = (target - pos) / spd
        
            if not stack or time > stack[-1]:
                stack.append(time)
        # else: merge (do nothing)
    
        return len(stack) 