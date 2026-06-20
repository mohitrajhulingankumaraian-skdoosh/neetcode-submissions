class Solution:
    def isPalindrome(self, s: str) -> bool:
        i, j = 0, len(s)-1
        while i < j:
            while i<len(s) and not s[i].isalnum():
                i += 1
            while j >= 0 and not s[j].isalnum():
                j -= 1
            if i <= j:
                if (s[i].isdigit() and not s[j].isdigit()) or (not s[i].isdigit() and s[j].isdigit()):
                    return False
                if s[i].isdigit() and s[i] != s[j]:
                    return False
                if not s[i].isdigit() and s[i].lower() != s[j].lower():
                    return False

            i += 1
            j -= 1
        
        return True