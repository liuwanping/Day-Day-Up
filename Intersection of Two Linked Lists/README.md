Problem:

Write a program to find the node at which the intersection of two singly linked lists begins.


For example, the following two linked lists:

A:          a1 → a2
                   ↘
                     c1 → c2 → c3
                   ↗            
B:     b1 → b2 → b3
begin to intersect at node c1.


Notes:

If the two linked lists have no intersection at all, return null.
The linked lists must retain their original structure after the function returns.
You may assume there are no cycles anywhere in the entire linked structure.
Your code should preferably run in O(n) time and use only O(1) memory.


Solution1:

一开始自己的想法是把 

a1 → a2 → c1 → c2 → c3					
↑(指针headA)											
b1 → b2 → b3 → c1 → c2 → c3  		   
↑(指针headB)											

变成					
     a1 → a2 → c1 → c2 → c3
     ↑(指针headA)
 b1 → b2 → b3 → c1 → c2 → c3
↑(指针headB)
						
这就需要分别遍历A和B，计算出len(A)和len(B)，
然后判断len(A)和len(B)的大小，做差，并把较长的那个的head向后移动差值大小的位置，
这时候A和B的尾部已经对齐，开始同时从新head位置往后遍历，直至找打交叉点位置。


Solution2:

这是看discuss学到的方法，非常简洁好用！

思路是把 
a1 → a2 → c1 → c2 → c3 
↑(指针headA)
b1 → b2 → b3 → c1 → c2 → c3 
↑(指针headB)

变成     
a1 → a2 → c1 → c2 → c3 → b1 → b2 → b3 → c1 → c2 → c3
↑(指针headA)
b1 → b2 → b3 → c1 → c2 → c3 → a1 → a2 → c1 → c2 → c3
↑(指针headB)

方法是如果headA不为空：headA=headA.next，如果为空：headA=headB，这样就把两个链表接到一起了。
下面链表也是相同，这样只要一个while就可以解决。简单来说就是把a+c与b+c变成(a+c+b)+c与(b+c+a)+c。	 

						
