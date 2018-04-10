class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        for x in range(1,len(digits)+1):
        	temp = digits[-x]+1
        	if temp<=9:
        		digits[-x] = temp
        		return digits
        	else:
        		digits[-x] = temp-10
        digits.insert(0,1)
        return digits