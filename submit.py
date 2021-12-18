string = input()

l, u = 0, 0
for c in string:
	if c.isupper():
		u += 1
	else:
		l += 1

if l < u:
	print(string.upper())
else:
	print(string.lower())

