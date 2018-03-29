# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head
        
        dummy = ListNode(0)
        pre = dummy
        cur=head
        
        while cur!=None and cur.next!=None:
            nxt = cur.next.next
            cur.next.next = cur
            pre.next = cur.next
            cur.next = nxt
            pre = cur
            cur = nxt
        
        return dummy.next