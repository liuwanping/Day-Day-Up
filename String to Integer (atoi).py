def myAtoi(str):
	if not str:
		return 0

	i=0
	sign=1
	base=0
	INT_MAX=2147483647
	INT_MIN=-2147483648

	while str[i]==' ':
		i=i+1
	if str[i]=='-':
		sign=-1
		i=i+1
	elif str[i]=='+':
		i=i+1

	while i < len(str) and str[i] >= '0' and str[i] <= '9':
		if base//10>INT_MAX or (base//10==INT_MAX and int(str[i])>7):
			return INT_MAX if sign else INT_MIN
		base=base*10+int(str[i])
		i=i+1

	return base*sign

print(myAtoi("2147483648"))