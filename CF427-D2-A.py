n = int(input())
events = input().split()
events = [int(x) for x in events]

ans = 0

crimes = 0
police = 0

for i in range(0, n):
	if events[i] > 0:
		ans += crimes
		crimes = 0
		police += events[i]
	else:
		crimes += 1
		if police > 0:

			police -= 1
			crimes -= 1

ans += crimes
print(ans)