def insertion_sort(A):
	for i in range(len(A)):
		p = A[i]
		j = i-1
		while j>=0 and A[j]>p:
			A[j+1] = A[j]
			j = j-1
		A[j+1]=p


A = [1,3,9,7,2,5,4]
insertion_sort(A)
for x in range(len(A)):
	print(A[x])

