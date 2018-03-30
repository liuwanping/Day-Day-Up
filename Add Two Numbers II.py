# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1.val == 0 and l2.val == 0:
            return l1
        
        n1 = 0
        n2 = 0
        while l1!=None:
            n1 =n1*10+l1.val
            l1 = l1.next
        while l2!=None:
            n2 = n2*10+l2.val
            l2 = l2.next
            
        res = n1+n2
        dummy = ListNode(0)
        cur = dummy
        while res != 0:
            cur.next = ListNode(res%10) 
            cur = cur.next
            res = res/10
        
        cur = dummy.next
        pre = None
        while cur != None:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
            
        return pre
            
            
        
        