class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        result = []
        # Naive approach, sort each string in list, then append to dictionary 
        for i in range(0, len(strs)):
            # Sort chars in string elem
            str_sorted = "".join(sorted(strs[i]))
            if str_sorted not in groups:
                # Add key in for the sorted one if not in yet, 
                # And init a list for it with the original key inside
                groups[str_sorted] = [strs[i]]
            elif str_sorted in groups:
                # Key has already been added, append list
                groups[str_sorted].append(strs[i])
        
        # Convert dict to list
        result = list(groups.values())
        return result
            
        