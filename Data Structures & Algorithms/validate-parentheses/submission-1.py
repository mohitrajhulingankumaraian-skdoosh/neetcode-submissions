class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for ch in s:
            if ch in ('(', '{', '['):
                stack.append(ch)
                continue

            if len(stack) and ch == '}' and stack[-1] == '{':
                stack.pop()
            elif len(stack) and ch == ']' and stack[-1] == '[':
                stack.pop()
            elif len(stack) and ch ==')' and stack[-1] == '(':
                stack.pop()
            else:
                return False
        
        return True if not len(stack) else False
            
        