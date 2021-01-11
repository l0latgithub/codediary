class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        
        """
        Given the head of a sorted linked list, delete all nodes that have duplicate numbers,
        leaving only distinct numbers from the original list. Return the linked list sorted as well.
        """

        run = ListNode(0,head)
        ans = run

        while run.next and run.next.next:
            if run.next.val==run.next.next.val:
                while run.next and run.next.next and run.next.val==run.next.next.val:
                    run.next = run.next.next
                run.next = run.next.next
            else:
                run = run.next
        return ans.next