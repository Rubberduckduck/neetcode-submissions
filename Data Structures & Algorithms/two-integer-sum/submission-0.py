class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for i in range(0, len(nums)):
            difference = target - nums[i]
            if difference not in map:
                map[nums[i]] = i
            else:
                # Difference is in map, can return
                return [map[difference], i]
        