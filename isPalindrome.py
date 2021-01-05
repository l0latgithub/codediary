class Solution:
    def isPalindrome(self, head: ListNode) -> bool:

	"""
	Given a singly linked list, determine if it is a palindrome.
	"""
        
#         savlst = []
#         while head:
#             savlst.append(head.val)
#             head = head.next
        
#         return savlst==savlst[::-1]

        fast = head
        slow = fast
        
        rev = None 
        
        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next
        
        if fast:
            slow = slow.next
        
        while slow and slow.val==rev.val:
            slow = slow.next
            rev = rev.next
            
        return not slow