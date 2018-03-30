# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if head == None:
            return head
        
        cur = head
        while cur!=None:
            nxt = RandomListNode(cur.label)
            nxt.next = cur.next
            cur.next = nxt
            cur = cur.next.next
            
        cur = head
        while cur!=None:
            cur.next.random = cur.random.next if cur.random else None
            cur = cur.next.next
        dummy1 = RandomListNode(0)
        dummy2 = RandomListNode(0)
        
        ori = dummy1
        copy = dummy2
        cur = head
        while cur!=None:
            ori.next = cur
            copy.next = cur.next
            ori = ori.next
            copy = copy.next
            cur = cur.next.next
            
        ori.next = None
        copy.next = None
        
        return dummy2.next