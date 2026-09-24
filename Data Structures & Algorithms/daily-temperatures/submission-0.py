class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        past_temps = []
        result = [0] * len(temperatures)
        # Have 2 indicies, one for going through the temperatures array
        # One when popping in the stack
        for i in range(0, len(temperatures)):
            # Keep checking if the 
            # current temp is higher than the temp stack's temperatures
            while len(past_temps) != 0 and temperatures[i] > temperatures[past_temps[-1]]:
                # Calculate indicies difference bef popping and add to result stack
                days_diff = i - past_temps[-1]
                result[past_temps[-1]] = days_diff
                past_temps.pop()
            
            # Add current temp index into the past temp stack
            past_temps.append(i)

        return result
            




        