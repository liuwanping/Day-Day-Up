Problem:

Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

For example,
Given 1->4->3->2->5->2 and x = 3,
return 1->2->2->4->3->5.

===============================

Solution:

非常可惜，思路是正确的，败在了两个小细节上。

(1)记录两个list的头，在初始的时候令head等于接下来要移动的指针就可以了呀，最后要用的时候直接用left_head.next或者right_head.next就可以了。

left_head = left = ListNode(0)

right_head = right = ListNode(0) 

(2)尾节点的next指向空节点。

right.next = None

