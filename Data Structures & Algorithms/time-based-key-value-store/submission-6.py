class TimeMap:

    time_map = {}

    def __init__(self):
        self.time_map = {}        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.time_map:
            self.time_map[key] = []

        self.time_map[key].append([value, timestamp]) 
        

    def get(self, key: str, timestamp: int) -> str:

        # Key does not exist
        if key not in self.time_map:
            return ""

        left = 0
        right = len(self.time_map[key]) - 1
        best_value = ""
        # We can do a binary search within the timestamps?
        if key in self.time_map:
            # Right is the highest timestamp available

            if timestamp > self.time_map[key][-1][1]:
                return self.time_map[key][-1][0]

            while left <= right:

                mid = (left + right) // 2

                if self.time_map[key][mid][1] == timestamp:
                    return self.time_map[key][mid][0]
                
                elif self.time_map[key][mid][1] < timestamp:
                    # Remember best value before shifting pointers
                    best_value = self.time_map[key][mid][0]
                    left = mid + 1
                else:
                    # Only remember the best value when smaller than the timestamp
                    right = mid - 1

        return best_value
        
