class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        para = paragraph.lower()
        pa = para.replace(',','')
        pa = pa.replace('.','')
        pa = pa.replace('!','')
        pa = pa.replace('?','')
        pa = pa.replace(':','')
        pa = pa.replace(';','')
        pa = pa.replace("'",'')
        wordlist = pa.split(' ')
        wordset = set(wordlist)
        wordcount = {}

        for k in wordset:
        	wordcount[k] = wordlist.count(k)
        maxcount = 0
        res = ''
        for key,value in wordcount.items():
        	if value>maxcount and key not in banned:
        		maxcount = value
        		res = key
        return res