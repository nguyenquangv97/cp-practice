string = input()
Smoves = 0
start = 0
for i in range(len(string)):
	index = ord(string[i]) - 97 # to make a = 0
	walk = abs(start - index)
	if walk < 13:
		Smoves += walk 
	else:
		Smoves += 26 - walk
	start = index
print(Smoves)

