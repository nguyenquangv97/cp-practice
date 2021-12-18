n, x = map(int, input().split())
distress = 0
for i in range(n):
	a = input().split()
	
	if a[0] == '+':
		x += int(a[1])
	else:
		if x < int(a[1]):
			distress += 1
		else:
			x-= int(a[1])

print(x, distress)