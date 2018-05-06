class Solution(object):
    def largeGroupPositions(self, S):
        """
        :type S: str
        :rtype: List[List[int]]
        """
        p = ''
        count = 0
        res = []
        i = -1
        for s in S:
        	i +=1
        	if p != s:
        		if count>=3:
        			res.append([begin,begin+count-1])
        		p = s
        		count = 1
        		begin = i
        	else:
        		count +=1
        return res


