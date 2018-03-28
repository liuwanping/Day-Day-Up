# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy1 = ListNode(0)
        dummy2 = ListNode(0)
        odd = dummy1
        even = dummy2
        while head!=None:
            odd.next = head
            even.next = head.next
            odd = odd.next
            even = even.next
            head = head.next.next if even else None
        odd.next = dummy2.next
        return dummy1.next
        
        #time out,but don't konw why
        # if head == None or head.next == None:
        #     return head
        # dummy = ListNode(0)
        # q = dummy
        # p = head
        # pre = None
        # while p!=None and p.next!=None:
        #     q.next = p.next
        #     q = q.next
        #     p.next = p.next.next
        #     pre = p
        #     p = p.next
        # if p==None:
        #     pre.next = dummy.next
        # else:
        #     p.next = dummy.next
        # return head
        