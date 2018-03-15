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

        if head == None:
            return head
        pre = ListNode(0)
        fh = ListNode(0)

        pre.next = head
        fh = pre

        while head:
        	while head!=None and head.val==val:
        		head=head.next
        	if head!=None:
        		pre.next=head
        		pre=pre.next
        		head=head.next
        	else:
        		pre.next=head

                
        return fh.next      

