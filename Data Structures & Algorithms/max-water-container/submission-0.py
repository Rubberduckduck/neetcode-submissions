class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        left = 0
        right = len(heights) - 1
        while left < right:
            # Width for container
            width = abs(right - left)
            # Have to use the lower height, as water will overflow if higher height?
            height = min(heights[right], heights[left])
            curr_area = width * height
            if curr_area > max_area:
                # Assign bigger current area for max possible area
                max_area = curr_area
            # Iterate only the pointer with lower height
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        
        return max_area

        