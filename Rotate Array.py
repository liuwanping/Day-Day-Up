# Rotate an array of n elements to the right by k steps.

# For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4].

# Note:
# Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.

# [show hint]

# Hint:
# Could you do it in-place with O(1) extra space?

class Solution(object):
    
    def reverse_list(self,nums,left,right):
        while left<right:
            tmp = nums[left]
            nums[left] = nums[right]
            nums[right] = tmp
            left +=1
            right -=1
            
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        k = k%length
        self.reverse_list(nums,0,length-1)
        self.reverse_list(nums,0,k-1)
        self.reverse_list(nums,k,length-1)
        

            
                
