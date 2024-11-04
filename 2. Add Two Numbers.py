class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Create a dummy node to serve as the start of the result linked list
        dummy_head = ListNode(0)
        current = dummy_head
        carry = 0
        
        # Traverse both linked lists until the end
        while l1 or l2 or carry:
            # Get the values from the current nodes, or 0 if the node is None
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            # Calculate the sum and carry
            total_sum = val1 + val2 + carry
            carry = total_sum // 10
            current.next = ListNode(total_sum % 10)
            
            # Move to the next nodes in the lists, if available
            current = current.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
        # Return the result linked list, starting from the first real node
        return dummy_head.next
