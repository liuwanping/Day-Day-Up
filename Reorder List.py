# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if head == None or head.next == None or head.next.next == None:
            return
        
        #find middle of list
        slow = head
        fast = head
        while fast!=None and fast.next!=None and fast.next.next!=None:
            slow =slow.next
            fast = fast.next.next
        
        r = slow.next
        slow.next = None
        
        #reverse right_half_list
        dummy = None
        pre = dummy
        while r!=None:
            nxt = r.next
            r.next = pre
            pre = r
            r = nxt
        
        #merge left_half_list and right_half_list
        left_head = head
        right_head = pre
        while right_head!=None and left_head!=None:
            left_nxt = left_head.next
            left_head.next = right_head
            
            right_nxt = right_head.next
            right_head.next = left_nxt
            
            left_head = left_nxt
            right_head = right_nxt
        

            
            
        
        

        
            
        
        