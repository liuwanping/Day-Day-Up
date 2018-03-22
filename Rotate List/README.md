problem:

Given a list, rotate the list to the right by k places, where k is non-negative.


Example:

Given 1->2->3->4->5->NULL and k = 2,

return 4->5->1->2->3->NULL.

========================================

Solution:

问题卡在对问题的理解上，正确的理解应该是这样的：

例如
 
12345,k=1 -> 51234

12345,k=2 -> 45123

12345,k=3 -> 34512

12345,k=4 -> 23451

12345,k=5 -> 12345

12345,k=6 -> 51234

......

也就是说，即使 k>len(list), 也是可以正确运转的, 由于存在循环，即求出 k%len(list) 往下用两个指针fast和slow找到对应的两个位置就可以了。
