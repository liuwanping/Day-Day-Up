# Given numRows, generate the first numRows of Pascal's triangle.

# For example, given numRows = 5,
# Return

# [
#      [1],
#     [1,1],
#    [1,2,1],
#   [1,3,3,1],
#  [1,4,6,4,1]
# ]
class Solution(object):
    #solution1:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1],[1,1]]
        res = [[1],[1,1]]
        for x in range(1,numRows-1):
            last = res[-1]
            new = []
            for y in range(x):
                new.append(last[y]+last[y+1])
            new.insert(0,1)
            new.append(1)
            res.append(new)
        return res

    #solution2:
    def generate(self, numRows):
        res = [[1]]
        for i in range(numRows-1):
            res += [map(lambda x,y:x+y,[0]+res[-1],res[-1]+[0])]
        return res[0:numRows]


# l = [9,2,3]
# print(sum(l[0:1]))
# print([1]+l+[8])