# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
   
        left_head = left = ListNode(0)
        right_head = right = ListNode(0)       
                
        while head!=None:
            if head.val<x:
                left.next = head
                left = left.next
            else:
                right.next = head
                right = right.next
            head = head.next
        
        right.next = None
        left.next = right_head.next
        
        return left_head.next
        
        
                
                