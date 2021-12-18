n, k = map(int, input().split())
t = (n + 1) // 2
print(2 * k - [1, 2 * t][k > t])


'''


n, k = map(int, input().split())

mid = n // 2
if n % 2 == 1:
	mid += 1
if k <= mid:
	print(2 * k - 1)
else:
	print((k - mid) * 2)

'''
