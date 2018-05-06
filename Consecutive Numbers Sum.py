class Solution(object):
    def consecutiveNumbersSum(self, N):
        """
        :type N: int
        :rtype: int
        """
        n = 1
        count = 0
        while n <= N//2+1:
        	mid = N//n
        	if n%2 != 0 :
        		if (mid-n//2)<=0:
        			break
        		if N == mid*n and (mid-n//2)>0:
        			count +=1
        	else:
        		if (mid-n//2)<0:
        			break
        		if N == mid*n+n/2 and (mid-n//2)>=0:
        			count +=1
        	n += 1
        return count

