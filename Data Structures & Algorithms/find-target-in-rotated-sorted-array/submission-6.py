class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:

            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            # Lhs sorted
            elif nums[left] <= nums[mid]:
                # Check if target lies in this range
                if target >= nums[left] and target < nums[mid]:
                    right = mid - 1
                # Not in above range
                else:
                    left = mid + 1
            
            # RHS sorted
            elif nums[right] >= nums[mid]:
                # Check if target lies in this range
                if target > nums[mid] and target <= nums[right]:
                    left = mid + 1
                # Not in above range
                else:
                    right = mid - 1
        
        return -1


        