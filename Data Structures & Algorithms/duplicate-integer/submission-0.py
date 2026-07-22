class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        seen = set()
        for i in range(0, len(nums)):
            # Append elems to set if not in set yet
            if nums[i] not in seen:
                seen.add(nums[i])
        # If list is not same size as the set, means got duplicate
        return len(seen) != len(nums)
        