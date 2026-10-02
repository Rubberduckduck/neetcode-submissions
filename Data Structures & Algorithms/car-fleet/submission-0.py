class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Time = (target - position) / speed
        # So we iterate through both arrays using one index only?
        # We need to sort the speed array in descending?

        fleet_times = []

        # We combine the 2 arrays into one array of pairs
        cars_pos_speed = []
        for i in range(0, len(position)):
            cars_pos_speed.append([position[i], speed[i]])
        
        # Sort the array in descending order
        cars_pos_speed.sort(key=lambda x: x[0], reverse = True)

        # Check if cars are in fleets
        for i in range(0, len(cars_pos_speed)):
            # Find time to reach target, then add to stack
            curr_time = (target - cars_pos_speed[i][0]) / cars_pos_speed[i][1]

            # Check car in front has time greater or equal than the curr car
            # Using stack top elem as the car on top
            if fleet_times and curr_time <= fleet_times[-1]:
                continue
            else:
                # New fleet time
                fleet_times.append(curr_time)
        
        return len(fleet_times)
            

        