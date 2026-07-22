class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        while left < len(s) and right >= 0:
            # Sanity checks, move indexes when encounter punctuations
            if not s[left].isalnum():
                left += 1
                continue
            if not s[right].isalnum():
                right -= 1
                continue
            # Make all lower before comparing
            lower_left = s[left].lower()
            lower_right = s[right].lower()
            if lower_left != lower_right:
                return False
            # Iteration
            left += 1
            right -= 1

        return True
        