# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        prev = None

        while(current):

            # Get the next node so it does not get lost later on
            next_node = current.next
            # Now we go backwards
            current.next = prev
    
            prev = current
            current = next_node
            
        
        return prev


        