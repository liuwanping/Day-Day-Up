class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # a faster method
        lastNonZeroIndex = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[lastNonZeroIndex] = nums[i]
                lastNonZeroIndex +=1
        for i in range(lastNonZeroIndex,len(nums)):
            nums[i] = 0
        
        #my slow method
#         length = len(nums)
#         if nums == None or length == 0:
#             return 
#         for i in range(length):
#             if nums[i] == 0:
#                 j = 0
#                 for j in range(i+1,length):
#                     if nums[j] !=0:
#                         nums[i] = nums[j]
#                         nums[j] = 0
#                         break
#                 if j == length:
#                     break
            
                
                
