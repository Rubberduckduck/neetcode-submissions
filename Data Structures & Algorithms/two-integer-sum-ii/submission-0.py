class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Use 2 pointers and iterate from left and right
        left = 0
        right = len(numbers) - 1
        result = []
        while left < len(numbers) and right >= 0:
            # Check the sum
            curr = numbers[left] + numbers[right]
            if curr == target:
                return [left + 1, right + 1]
            if curr < target:
                # If current is lesser, increment lhs
                left += 1
            elif curr > target:
                # If current is more, decerment rhs
                right -= 1


        