class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        dummy = ListNode()
        dummy.next = head