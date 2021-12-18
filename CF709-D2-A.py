n, b, d = map(int, input().split())
oranges = list(map(int, input().split()))
sum = 0
waste = 0
for i in range(n):
	if oranges[i] <= b:
		sum += oranges[i]
		if sum > d:
			sum = 0
			waste += 1

print(waste)