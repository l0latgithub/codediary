class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
	
	"""
	Given the head of a sorted linked list, delete all duplicates such 
	that each element appears only once. Return the linked list sorted as well.
	"""
        
        run = ListNode(0,head)
        ans = run
        
        while run.next and run.next.next:
            if run.next.val==run.next.next.val:
                run.next = run.next.next
            else:
                run = run.next
                
        return ans.next