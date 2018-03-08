# def searchInsert( nums, target):
# 	if target<nums[0]:
# 		return 0
# 	elif target>nums[-1]:
# 		return len(nums)
# 	else:
# 		for num in nums:
# 			if target == num or num > target:
def searchInsert( nums, target):
	l=0
	r=len(nums)-1
	while True:
		m=(l+r)//2
		if target<nums[m]:
			r=m-1
			if r>=0:
				if target == nums[r]:
					return r
				elif target>nums[r]:
					return r+1
			else:
				return 0
		elif target>nums[m]:
			l=m+1
			if l<len(nums):
				if target<=nums[l]:
					return l
			else:
				return len(nums)
		else:
			return m


nums=[1,3,5]
target=2
print(searchInsert(nums,target))