Problem:

Reverse a singly linked list

===========================

Solution:

前几天做判断是否是回文串的题目，遇到过这个问题，刚刚做完，所以一次就通过了，可以说非常开心了，所以说还是要多多练习才能进步吖~

首先要在head前面加一个指向None的指针，然后依次向后遍历即可，突然觉得文字不如代码清晰，那就贴段代码吧。

def reverseList(self, head):

	"""
	
	:type head: ListNode
	
	:rtype: ListNode
	
	"""
	
	pre = None
	
	while head:
	
		nxt = head.next
		
		head.next = pre
		
		pre = head
		
		head = nxt
		
	return pre
