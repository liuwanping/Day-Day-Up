def firstBadVersion(n):
	if isBadVersion(1):
		return 1
	elif not isBadVersion(n):
		return n
	l = 0
	r = n-1
	while l<=r:
		m=(l+r)//2
		if isBadVersion(m) and not isBadVersion(m-1):
			return m
		elif not isBadVersion(m) and isBadVersion(m+1):
			return m+1
		elif isBadVersion(m) and isBadVersion(m-1):
			r=m-1
		elif not isBadVersion(m) and not isBadVersion(m+1):
			l=m+1
