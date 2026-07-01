class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        results = [0]*len(temperatures)
        for i in range(1, len(temperatures)):
            if temperatures[i-1] >= temperatures[i]:
                stack.append((temperatures[i-1], i-1))
            
            else:
                results[i-1] = 1
                while len(stack) and stack[-1][0] < temperatures[i]:
                    temp, idx = stack.pop()
                    results[idx] = i - idx
        
        return results


        
        