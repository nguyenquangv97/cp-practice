n = int(input())
a = list(map(int, input().split()))
b = [-1] * n

for i, x in enumerate(a):
	b[x-1] = i + 1

print(*b)