ans = 0
n = int(input())
home = []
guest = []
res = 0
for i in range(n):
	x = input().split()
	home.append(x[0])
	guest.append(x[1])


for i in range(len(home)):
	for j in range(len(guest)):
		if home[i] == guest[j]:
			res += 1

print(res)