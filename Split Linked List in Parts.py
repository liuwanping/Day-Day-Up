# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def splitListToParts(self, root, k):
        """
        :type root: ListNode
        :type k: int
        :rtype: List[ListNode]
        """
        cur = root
        length = 0
        while cur!=None:
            length += 1
            cur = cur.next
        
        sublen = length/k
        mod = length%k
        reslist = []
        pre = None
        for y in range(k):
            reslist.append(root)
            if root!=None:
                for x in range((sublen+1) if mod>0 else sublen):
                    pre = root
                    root = root.next
                pre.next = None
                mod -= 1
        return reslist
        