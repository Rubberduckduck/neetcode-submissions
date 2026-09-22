class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        # One stack for op one stack for num
        num_stack = []

        for i in range(0, len(tokens)):
            # Use try except for int conversion
            try:
                # If is number, append to stack
                num_stack.append(int(tokens[i]))
            except:
                if len(num_stack) >= 2:
                    # Is operator, not num
                    first_num = num_stack.pop()
                    second_num = num_stack.pop()
                    if tokens[i] == "+":
                        curr_result = first_num + second_num
                        # Add result back to the stack
                        num_stack.append(curr_result)
                    elif tokens[i] == "-":
                        curr_result = second_num - first_num
                        # Add result back to the stack
                        num_stack.append(curr_result)
                    elif tokens[i] == "*":
                        curr_result = first_num * second_num
                        # Add result back to the stack
                        num_stack.append(curr_result)
                    elif tokens[i] == "/":
                        # Divs by 0
                        if second_num == 0:
                            second_num = 1
                        curr_result = int(second_num / first_num)
                        # Add result back to the stack
                        num_stack.append(curr_result)
        
        # Final result is 
        return num_stack.pop()

        