# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        """
        Given the head of a singly linked list, reverse the list, and return the reversed list.
        """
#         run = head
#         rev = None
        
#         while run:
#             rev, rev.next, run=run, rev, run.next
            
#         return rev
        return self.selfrev(head)

    def selfrev(self, node, prev=None):
        
        if not node:
            return prev
        
        nxt = node.next
        node.next = prev
        return self.selfrev(nxt, node)