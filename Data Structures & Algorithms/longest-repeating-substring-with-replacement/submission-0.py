class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Window set up
        left = 0
        right = 0
        max_length = 0
        letter_counter = {}
        while left < len(s) and right < len(s):
            # Update the character freq count in dict
            letter_counter[s[right]] = letter_counter.get(s[right], 0) + 1
            
            # We check for the most freq char in the dict
            highest_freq = max(letter_counter.values())

            # Number of chars to replace
            win_len = right - left + 1
            num_char_replace =  win_len - highest_freq

            # Check number of chars to replace higher than k
            if num_char_replace > k:
                # If higher, shrink window
                letter_counter[s[left]] -= 1
                left += 1
                right += 1
            else:
                # Update max window length, then increment right
                max_length = max(max_length, win_len)
                right += 1

        
        return max_length
