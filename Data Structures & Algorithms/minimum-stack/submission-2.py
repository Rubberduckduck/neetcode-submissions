class MinStack:

    def __init__(self):
        self.stack = []
        self.stack_min = 2**1000
        

    def push(self, val: int) -> None:
        # We push the curr stack min as a pair
        # And for every push we will check for the min to be assigned
        if val < self.stack_min:
            self.stack_min = val
        self.stack.append([val, self.stack_min])
        

    def pop(self) -> None:
        # We need to update the new min again after it gets popped
        # If the pop elem was the min
        print("Bef pop: ", self.stack_min)
        pop_elem = self.stack.pop()
        if len(self.stack) != 0:
            self.stack_min = self.stack[-1][1]
        else:
            # Reset back the stack's min if stack only had 1 elem and it got popped
            self.stack_min =  2**1000
        print("After pop: ", self.stack_min)
        
        

    def top(self) -> int:
        return self.stack[-1][0]
        

    def getMin(self) -> int:
        # Newest elem at the top of stack will always be the new updated min
        return self.stack[-1][1]
        
