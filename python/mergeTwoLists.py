class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        """
        Merge two sorted linked lists and return it as a sorted list. 
        The list should be made by splicing together the nodes of the first two lists.
        """
        
        run = ListNode()
        ans = run
        
        while l1 and l2:
            if l1.val<l2.val:
                run.next = l1
                l1 = l1.next
            else:
                run.next = l2
                l2 = l2.next
            run = run.next
        run.next = l1 or l2
        return ans.next