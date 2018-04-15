# Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

# Example:

# Given array nums = [-1, 2, 1, -4], and target = 1.

#time out O(n^3)
The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        closest = nums[0]+nums[1]+nums[2]
        length = len(nums)
        for i in range(length):
            for j in range(i+1,length):
                for k in range(j+1,length):
                    sum3 = nums[i]+nums[j]+nums[k]
                    tmp = abs(sum3-target)
                    cur = abs(closest - target)
                    closest = sum3 if tmp<cur else closest
        return closest

#accepted O(n^2)
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        length = len(nums)
        res = nums[0]+nums[1]+nums[2]
        for i in range(length-2):
            l = i+1
            r = length-1
            while l<r:
                cur = nums[i]+nums[l]+nums[r]
                if cur == target:
                    return cur
                if abs(cur-target) < abs(res-target):
                    res = cur
                if cur < target:
                    l += 1
                elif cur > target:
                    r -= 1
        return res


s = Solution()
nums = [-1, 2, 1, -4]
print(s.threeSumClosest(nums,1))