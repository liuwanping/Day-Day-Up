# Given an index k, return the kth row of the Pascal's triangle.

# For example, given k = 3,
# Return [1,3,3,1].

# Note:
# Could you optimize your algorithm to use only O(k) extra space?

class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """ 
        res = [1]
        for x in range(rowIndex):
            #res = list(map(lambda x,y:x+y,[0]+res,res+[0]))
            res = [x+y for x,y in zip([0]+res,res+[0])]
        return res
        
# s = Solution()
# l = s.getRow(3)
# print(l)

listx = [1,2,5]
listy = [4,7,2]

print(list(map(lambda x,y : x+y,listx,listy)))
