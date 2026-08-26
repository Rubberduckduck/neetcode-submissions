class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        prefix_array = [1] * len(nums) 
        suffix_array = [1] * len(nums) 
        result = []

        # Populate prefix array from left to right
        for i in range(1, len(nums)):
            product = nums[i-1] * prefix_array[i-1]
            prefix_array[i] = product

        # Populate prefix array from left to right
        for i in range(len(nums)-2, -1, -1):
            product = nums[i+1] * suffix_array[i+1]
            suffix_array[i] = product

        for i in range(0, len(nums)):
            result.append(prefix_array[i] * suffix_array[i])
        
        return result

        