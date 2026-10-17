class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        # We make last elem to be right ptr
        right = len(nums) - 1
        while left < right:
            mid = (left + right) // 2

            # Check if min is rhs or lhs
            if nums[right] < nums[mid]:
                left = mid + 1
            else:
                # Element could be the mid index, dont discard
                right = mid
        
        return nums[left]
            



        