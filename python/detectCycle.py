class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        
        """
        Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

        There is a cycle in a linked list if there is some node in the list that can be reached again
        by continuously following the next pointer. Internally, pos is used to denote the index of the
        node that tail's next pointer is connected to. Note that pos is not passed as a parameter.
        
        """
        
        fast = head
        slow = fast
        
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            
            if fast==slow:
                fast = head
                while fast!=slow:
                    fast=fast.next
                    slow=slow.next
                return fast
        else:
            return None