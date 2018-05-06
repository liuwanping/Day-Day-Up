import re
class Solution(object):
    def maskPII(self, S):
        """
        :type S: str
        :rtype: str
        """
        info = S.lower()
        info = re.sub('[^A-Za-z0-9@.]+', '', info)
        if '@' in info:
        	i = info.index('@')
        	return info[0]+"*****"+info[i-1:len(info)]
        if len(info)>=13:
        	return "+***-***-***-"+info[-4:]
        elif len(info)>=12:
        	return "+**-***-***-"+info[-4:]
        elif len(info)>=11:
            return "+*-***-***-"+info[-4:]
        else:
            return "***-***-"+info[-4:]
            

s = Solution()
print(s.maskPII("(3906)2 07143 711"))
# s = "hello"
# print(s[-4:])