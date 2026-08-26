class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Empty list has a sequence of 0
        if not nums:
            return 0
        nums.sort()
        curr = 1
        longest = 1
        for i in range(1, len(nums)):
            # If duplicate, skip
            if nums[i] == nums[i-1]:
                continue
            # Increment streak
            if nums[i] == nums[i-1] + 1:
                curr += 1
            else:
                # Curr streak is broken, store into longest streak if is longest
                longest = max(curr, longest)
                # Reset streak
                curr = 1
        
        return max(curr, longest)

        