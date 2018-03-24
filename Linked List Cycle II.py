# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return head
        meet = self.isCycle(head)
        if meet == None:
            return None
        nxt = meet.next
        cycleNodes = 1
        while nxt!=meet:
            cycleNodes +=1 
            nxt = nxt.next
        slow = head
        fast = head
        for x in range(cycleNodes):
            fast = fast.next
        while True:
            if slow == fast:
                return slow
            slow = slow.next
            fast=fast.next
  
            
    def isCycle(self,head):
        slow = head
        fast = head
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return slow
        return None