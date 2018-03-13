class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def deleteDuplicates(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    # solution 1:
    if head==None or head.next==None:
        return head
    p=ListNode(0)
    q=ListNode(0)
    p=head
    q=head.next
    while p:
        q=p.next
        while q!=None and p.val==q.val:
            q=q.next
        p.next=q
        p=q
    return head


    # solution2
    current=ListNode(0)
    current=head
    while head!=None and head.next!=None:
        if head.val==head.next.val:
            head.next=head.next.next
        else:
            head=head.next

    return current

