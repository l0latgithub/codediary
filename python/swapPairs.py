class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        """
	Given a linked list, swap every two adjacent nodes and return its head.
	"""

        run = ListNode(0, head)
        ans = run
        
        while run.next and run.next.next:
            
            odd = run.next
            even = run.next.next
            
            odd.next = even.next
            even.next= run.next
            run.next = even
            
            run = even.next
        
        return ans.next