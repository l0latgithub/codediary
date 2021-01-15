class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        
        """
        Given the head of a linked list, remove the nth node from 
        the end of the list and return its head.
        """
        
        fast = ListNode(0, head)
        slow = fast
        ans = slow
        
        for _ in range(n):
            fast = fast.next
        
        while fast.next:
            fast = fast.next
            slow = slow.next
        
        slow.next = slow.next.next
        return ans.next