class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dups = set()
        left = 0
        right = 0
        max_length = 0
        while left < len(s) and right < len(s):
            if s[right] not in dups:
                # Char not in hash set, add in
                dups.add(s[right])
                max_length = max(max_length, right - left + 1)
                right += 1
            elif s[right] in dups:
                dups.remove(s[left])                
                left += 1
        return max_length


        