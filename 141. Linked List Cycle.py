class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        dummy = ListNode()
        dummy.next = head
        fast = slow = dummy
        
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast is slow:
                return True 
        return False
