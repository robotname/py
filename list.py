#!/c/Users/robotname/AppData/Local/Programs/Python/Python35-32/python
import random
m=[[random.randint(0,9999) for y in range (10)]for x in range (2)]
f=[[0 for x in range(10)] for y in range(10)]
for i in range (10):
	f[int(m[0][i]/1000)][int(m[1][i]/1000)]+=1

for y in range(10):
	for x in range(10):
		if f[x][y] > 0:
			print (f[x][y], "", end="")
		else:
			print(". ", end="")
	print("")