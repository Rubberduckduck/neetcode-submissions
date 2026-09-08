class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Sort the list
        nums.sort()
        result = []
        # Use i index to iterate, then use 2 pointers from right of i
        # I will be target, since (nums[j]+nums[k]) + (-nums[i]) = 0
        for i in range(0, len(nums)):
            # Reset pointers
            left = i + 1
            right = len(nums) - 1
            if nums[i] == nums[i-1] and i > 0:
                continue
            while left < right:
                target = nums[left] + nums[right]
                # Reached target, bring -nums[i] over to rhs, target == -nums[i]
                if target == -nums[i]:
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    # Checks for dups, slide to next available non dup number
                    while left < right and nums[left - 1] == nums[left]:
                        left += 1
                    while left < right and nums[right + 1] == nums[right]:
                        right -= 1
                # (nums[j]+nums[k]) < -nums[i], we need go bigger
                elif target < -nums[i]:
                    left += 1
                # (nums[j]+nums[k]) < target, we need go smaller
                elif target > -nums[i]:
                    right -= 1
        
        return result


        