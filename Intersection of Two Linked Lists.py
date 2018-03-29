# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
	#solution1
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        p=headA
        q=headB
        new_headA=headA
        new_headB=headB
        i=0
        j=0
        while p is not None:
        	i+=1
        	p=p.next
        while q is not None:
        	j+=1
        	q=q.next
        if i>j:
        	for x in range(i-j):
        		new_headA=new_headA.next
        elif i<j:
            for x in range(j-i):
        		new_headB=new_headB.next
        while new_headB != new_headA:
        	new_headA=new_headA.next
        	new_headB=new_headB.next
        return new_headA
        #solution2
        if headA==None or headB==None:
            return None
        curA,curB = headA,headB
        while curA!=curB:
            curA = curA.next if curA!=None else headB
            curB = curB.next if curB!=None else headA
        return curA
