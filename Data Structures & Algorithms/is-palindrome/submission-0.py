class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        new_str = "".join(char for char in s if char.isalnum()).lower()

        L, R = 0, len(new_str) - 1
        print(new_str)
        while L < R:
            if new_str[L] != new_str[R]:
                return False
            L += 1
            R -= 1
        return True