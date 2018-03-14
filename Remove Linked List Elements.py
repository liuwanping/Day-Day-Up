# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        cur = ListNode(0)
        pre = ListNode(0)
        fh = ListNode(0)
        pre.next = cur
        cur = head
        fh = pre
        while pre and cur:
        	cur=pre.next
        	if cur.val == val:
        		pre.next = cur.next
        		pre = pre.next
        	else:
        		pre=cur
                
        return fh.next      