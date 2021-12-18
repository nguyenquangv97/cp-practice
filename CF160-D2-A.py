n = int(input())
coins = sorted(list(map(int, input().split())))

current = res = 0
while current <= sum(coins):
	current += coins.pop()
	res += 1

print(res)