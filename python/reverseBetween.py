class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:

	"""
	Reverse a linked list from position m to n. Do it in one-pass.
	"""
        
        if m==n:
            return head
        
        run = ListNode(0, head)
        ans = run
        
        for i in range(m-1):
            run = run.next
        
        left = run.next
        mid = left.next
        right = mid.next
        
        
        for i in range(n-m):
            
            left.next = mid.next
            mid.next = run.next
            run.next = mid
            
            mid = right
            if right:
                right = right.next
        
        return ans.next
    