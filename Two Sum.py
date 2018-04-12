# Given an array of integers, return indices of the two numbers such that they add up to a specific target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# Example:

# Given nums = [2, 7, 11, 15], target = 9,

# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        #solution O(n^2)
        for x in range(len(nums)):
            for y in range(x+1,len(nums)):
                if nums[x]+nums[y] == target:
                    return [x,y]

        #solution O(n)
        dict_nums = {}
        for i in range(len(nums)):
            a = target - nums[i]
            if a in dict_nums:
                return [dict_nums[a],i]
            else:
                dict_nums[nums[i]]=i
        