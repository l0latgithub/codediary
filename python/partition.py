
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:

	"""
	Given the head of a linked list and a value x, partition it such that all nodes
	less than x come before nodes greater than or equal to x.

	You should preserve the original relative order of the nodes in each of the two partitions.
	"""
        
        sml = ListNode()
        big = ListNode()
        
        ans = sml
        mid = big
        
        run = head
        while run:
            if run.val<x:
                sml.next = run
                sml = sml.next
            else:
                big.next = run
                big = big.next
                
            run = run.next
        
        sml.next = mid.next
        big.next = None
        return ans.next