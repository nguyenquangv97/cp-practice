n = int(input())

group = 1

current = input()


for i in range(1, n):
	string = input()
	if current[1] == string[0]:
		group += 1

	current = string

print(group)
