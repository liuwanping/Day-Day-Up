# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        
        fast = head
        slow = head

        while fast and fast.next:
        	fast =fast.next.next
        	slow = slow.next


        half_head = self.reverseList(slow)

        while half_head and head:
        	if half_head.val!=head.val:
        		return False
        	else:
        		head = head.next
        		half_head = half_head.next
        return True

    def reverseList(self,slow):
    	pre = None
        
    	while slow:
    		nxt = slow.next
    		slow.next = pre
    		pre = slow
    		slow = nxt

    	return pre
