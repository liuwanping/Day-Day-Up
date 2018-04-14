# Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

# Note: You may not slant the container and n is at least 2.

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        #贪心算法 每一步选择最优 最后即是最优
        res = 0
        left = 0
        right = len(height)-1
        while(left<right):
            res = max(res,min(height[left],height[right])*(right-left))
            if height[left]<height[right]:
                left +=1
            else:
                right -=1
        return res

        #暴力循环 超时
        # length = len(height)
        # maxcont = 0
        # for i in range(length):
        #     for j in range(i+1,length):
        #         curcont = (j-i)*min(height[i],height[j])
        #         if  curcont > maxcont:
        #             maxcont = curcont
        # return maxcont
        