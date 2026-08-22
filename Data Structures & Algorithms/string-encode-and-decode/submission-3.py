class Solution:

    def encode(self, strs: List[str]) -> str:
        result = str()
        # Split the string with # and length of string
        for string in strs:
            result += f"{len(string)}#{string}"
        return result

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while i < len(s):
            # Find delim starting from char index
            delim = s.find("#", i)

            # Gets string length from curr index to delim index
            length = int(s[i:delim])

            # +1 from delim index to get to string
            i = delim + 1

            # Append string from current start string index(i) to end of string (i + length)
            result.append(s[i:i+length])

            i += length
            
        
        return result
