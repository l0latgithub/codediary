class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        """
        Write a program to find the node at which the intersection 
        of two singly linked lists begins.
        """
        if not headA or not headB:
            return None
        
        pa = headA
        pb = headB
        
        while pa!=pb:
            # print (pa, pb)
            # if either pointer hits the end, switch head and continue the second traversal, 
            # if not hit the end, just move on to next
            pa = headB if not pa else pa.next
            pb = headA if not pb else pb.next
        
        # only 2 ways to get out of the loop, they meet or the both hit the end=None
        return pa
