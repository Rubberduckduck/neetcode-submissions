class Solution:
    def isValid(self, s: str) -> bool:
        paren_stack = []
        closing_brackets = {')': '(', '}': '{', ']':'['}
        # Iterate through the string, push opening bracket into stack
        for elem in s:
            # Push opening brackets into stack
            if elem not in closing_brackets:
                paren_stack.append(elem)
            else:
                # Bracket is closing type
                if not paren_stack or paren_stack[-1] != closing_brackets[elem]:
                    return False
                # Pop matching bracket
                paren_stack.pop()

        return not paren_stack
            



