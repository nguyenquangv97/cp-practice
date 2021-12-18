n = int(input())
cakes = list(map(int, input().split()))
s = set()
for c in cakes:
	s.add(c)
	while n in s:
		print(n, end=' ')
		n -= 1
	print()
