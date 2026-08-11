class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # Dict to track frequency
        number_counters = {}

        for i in range(0, len(nums)):
            if nums[i] in number_counters:
                # If already existed, increment
                number_counters[nums[i]] += 1
            else:
                # Add to dictionary and set freq to 1
                number_counters[nums[i]] = 1
        
        # Sort the dictionary items by frequency in descending order
        # Example will be [1,2,2,3,3,3]
        # .items will return as tuple, x[1] is the frequency to sort
        # Hene output will be smth like: sorted_elements = [(3,3), (2,2), (1,1)]
        sorted_elements = sorted(number_counters.items(), key=lambda x: x[1], reverse=True)
        
        # Extract the top k keys
        result = []

        for i in range(k):
            result.append(sorted_elements[i][0])
            
        return result