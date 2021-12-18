n = int(input())
a = []
f = 0
for i in range(n):
	l = input().split()
	a += [l[0]]
	if l[0] != l[1]:
		f = 1
if f:
	print('rated')
elif a[::-1] == sorted(a, key=int):
	print('maybe')
else:
	print('unrated')
