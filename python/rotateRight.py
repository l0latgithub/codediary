class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        
        if k==0 or not head or not head.next:
            return head
        
        fast = ListNode(0, head)
        slow = fast
        ans = slow
        
        listlen = 0
        while fast.next:
            listlen+=1
            fast = fast.next
        
        k = k%listlen
        if k==0:
            return head
        
        for _ in range(listlen-k):
            slow = slow.next
        
        fast.next = ans.next
        ans.next = slow.next
        slow.next = None
        return ans.next