# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        
        """
        Given the head of a linked list and an integer val, remove all the nodes of 
        the linked list that has Node.val == val, and return the new head.
        """
        
        run = ListNode(0, head)
        ans = run
        
        while run.next:
            if run.next.val==val:
                run.next = run.next.next
            else:
                run = run.next
                
        return ans.next