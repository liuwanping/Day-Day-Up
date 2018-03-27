# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if head==None or head.next==None:
            return head
        
        dummy = ListNode(0)
        pre = dummy

        while head!=None:
            nxt = head.next
            if head.val<pre.val:
                pre = dummy
            while pre.next != None and head.val>pre.next.val:
                pre = pre.next
            head.next = pre.next
            pre.next = head
            head = nxt

        return dummy.next