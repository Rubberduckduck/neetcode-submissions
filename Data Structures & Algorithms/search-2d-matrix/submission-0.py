class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # We can use the first and last elements of each row to compare the target
        # If target falls in the range, we iterate the range to find the target

        # Else we -1 or +1 to the next row
        top = 0
        bot = len(matrix) - 1
        while top <= bot:

            # Binary search outer loop as well
            mid_outer = (bot + top) // 2

            row_size = len(matrix[mid_outer])

            # Get the first and last elem
            first_elem = matrix[mid_outer][0]
            last_elem = matrix[mid_outer][row_size - 1]

            if target >= first_elem and target <= last_elem:
                # We do a binary search in the row to find target
                left = 0
                right = row_size - 1
                while left <= right:
                    mid = (right + left) // 2
                    # Check if larger or smaller than target
                    if matrix[mid_outer][mid] == target:
                        return True
                    elif matrix[mid_outer][mid] > target:
                        right = mid - 1
                    elif matrix[mid_outer][mid] < target:
                        left = mid + 1
                
                # Target was supposed to be in this row, but not found
                return False
            elif target > first_elem:
                top = mid_outer + 1
            elif target < last_elem:
                bot = mid_outer - 1
        
        return False