# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """

        dummy = ListNode(0)
        dummy.next = head
        pre = dummy

        for x in range(m-1):
        	pre = pre.next

        reverse = None
        cur = pre.next

        for x in range(n-m+1):
        	nxt = cur.next
        	cur.next = reverse
        	reverse = cur
        	cur = nxt

        pre.next.next = cur
        pre.next = reverse

        return dummy.next




