import random
def generate_rand(n, sum_v):
    Vector = [random.random() for i in range(n)]
    Vector = [ int(i / sum(Vector) * sum_v) for i in Vector]
    cha = 0
    if sum(Vector) < sum_v:
        cha = sum_v-sum(Vector)
    count = 0
    for x in Vector:
    	if x == 0:
    		count += 1
    for i in range(n):
    	if Vector[i] == 0:
    		Vector[i] = int(Vector[i]+cha//count)
    if sum(Vector)<sum_v:
    	Vector[0] += sum_v - sum(Vector)
    return Vector

l = generate_rand(200,1000)
for i in range(1000):
	print(1)
print(sum(l))
print(len(l))
print(max(l))
