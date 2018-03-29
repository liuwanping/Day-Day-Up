# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head ==None or k==0:
        	return head
        
        q = head
        p = head
        new_head = head
        length = 1
        
        while q.next!=None:
        	length +=1
        	q=q.next

        rotatek = k%length

        for x in range(length-rotatek-1):
        	p = p.next
            
        if p.next!=None:
            new_head = p.next
        
        q.next = head
        p.next = None

        return new_head

