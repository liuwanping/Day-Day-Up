# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def deleteDuplicates(self, head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    pre=ListNode(0)
    cur=ListNode(0)
    fh=ListNode(0)
    pre.next=head
    cur=head
    fh=pre
    while cur!=None:
    	while cur.next!=None and cur.val==cur.next.val:
    		cur=cur.next
    	if pre.next==cur:
    		fh.next=cur
    		fh=fh.next
    		pre=pre.next
    	else:
    		pre=cur
    		cur=cur.next
    return 