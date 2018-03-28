# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
        	return head

        slow = head
        fast = head
        while fast !=None and fast.next != None and fast.next.next != None:
        	slow = slow.next
        	fast = fast.next.next

        nxt = slow.next
        slow.next = None

        l1 = self.sortList(head)
        l2 = self.sortList(nxt)
        return self.merge(l1,l2)


    def merge(self,slow,fast):
    	l = ListNode(0)
    	p = l
    	while slow!=None and fast!=None:
    		if slow.val<=fast.val:
    			l.next = slow
    			slow = slow.next
    		else:
    			l.next = fast
    			fast = fast.next
    		l = l.next
    	if slow != None:
    		l.next = slow
    	if fast != None:
    		l.next = fast
    	return p.next