class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # If the number of banana less than k, need match k
        # So we need set our own min k, brute force is to iterate through whole array?
        # We set the lowest rate as 1 first
        lower_bound = 1

        # Highest rate will be highest in the pile
        higher_bound = max(piles)

        # Binary search betw the highest and lowest
        while lower_bound < higher_bound:
            mid = (lower_bound + higher_bound) // 2
            # Iterate thrpugh piles and get total time
            total_time = 0
            for i in range(0, len(piles)):
                pile_time = math.ceil(piles[i] / mid)
                total_time += pile_time
            
            # Now we check if total_time within range
            if total_time <= h:
                # We save this timing first, and check if there is a faster time
                higher_bound = mid
            elif total_time > h:
                # Shift lower boundary, need faster time
                lower_bound = mid + 1
        
        return lower_bound






        