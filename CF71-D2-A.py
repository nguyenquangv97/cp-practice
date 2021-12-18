n = int(input())
for i in range(n):
	string = input()

	if len(string) <= 10:
		print(string)
	else:
		print(string[0] + str(len(string[1: -1])) + string[-1])
