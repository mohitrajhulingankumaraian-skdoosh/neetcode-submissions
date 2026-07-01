class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(list(zip(position, speed)), key = lambda x: x[0])
        stack = []
        for c in cars:
            while stack and (target - c[0])/c[1] >= (target - stack[-1][0])/stack[-1][1]:
                stack.pop()
            stack.append(c)
        
        return len(stack)

        