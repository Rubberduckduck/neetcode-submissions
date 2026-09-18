class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Use 2 dict to count freq?
        s1_freqs = {}
        s2_freqs = {}

        for i in range(0, len(s1)):
            # If the freq exist, add 1, else assign 0 then add 1
            s1_freqs[s1[i]] = s1_freqs.get(s1[i], 0) + 1

        left = 0
        right = 0
        while right < len(s2):
            # We increase the window if the char is in s1, then slide accross?
            s2_freqs[s2[right]] = s2_freqs.get(s2[right], 0) + 1
            # Check window wize if more than s1 len
            if right - left + 1 > len(s1):
                s2_freqs[s2[left]] -= 1
                # Drop key when freq = 0
                if s2_freqs.get(s2[left]) == 0:
                    s2_freqs.pop(s2[left], None)
                left += 1
            # When window matches to the substring s1, return true
            if s2_freqs == s1_freqs:
                return True
            
            # Expand window
            right += 1

        return False
